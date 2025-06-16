from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import httpx
import json
from cachetools import LRUCache
import logging
from tenacity import retry, stop_after_attempt, wait_fixed, retry_if_exception_type
from typing import Optional, Dict, Any
import hashlib
import os
from abc import ABC, abstractmethod

# Load environment variables from .env file
from dotenv import load_dotenv

from constants.category_handler import CategoryHandler
from constants.category_registry import CategoryRegistry
from constants.finance_labels import FinanceCategoryHandler
from constants.healthcare_insurance import HealthcareInsuranceCategoryHandler
from constants.investment_labels import InvestmentCategoryHandler
from constants.real_estate import RealEstateCategoryHandler
load_dotenv()

# FastAPI app
app = FastAPI(title="Text Classification API", version="1.0.0")

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# API configuration
API_URL = os.getenv("API_URL")
HEADERS = {"Content-Type": "application/json"}

# Cache setup (LRU cache with 1000 entries)
cache = LRUCache(maxsize=1000)

# Retry configuration
MAX_RETRIES = 3
RETRY_DELAY = 2


# Initialize category registry
category_registry = CategoryRegistry()
category_registry.register("finance", FinanceCategoryHandler())
category_registry.register("investment", InvestmentCategoryHandler())
category_registry.register("real_estate", RealEstateCategoryHandler())
category_registry.register("healthcare_insurance", HealthcareInsuranceCategoryHandler())

# Request model
class ClassificationRequest(BaseModel):
    data: dict
    category: str
    model: str = "meta-llama/Meta-Llama-3.1-8B-Instruct"

# Cache key generator
def generate_cache_key(request: ClassificationRequest) -> str:
    """Generate a cache key based on the request body."""
    request_str = json.dumps(request.dict(), sort_keys=True)
    return hashlib.md5(request_str.encode('utf-8')).hexdigest()

# Async HTTP client for API calls
async def make_api_call(payload: dict) -> dict:
    async with httpx.AsyncClient(timeout=30.0) as client:
        response = await client.post(API_URL, headers=HEADERS, json=payload)
        response.raise_for_status()
        return response.json()

# Retryable classify function
@retry(
    stop=stop_after_attempt(MAX_RETRIES),
    wait=wait_fixed(RETRY_DELAY),
    retry=retry_if_exception_type((httpx.RequestError, httpx.HTTPStatusError)),
    before_sleep=lambda retry_state: logger.info(
        f"Retrying attempt {retry_state.attempt_number}/{MAX_RETRIES} after {RETRY_DELAY}s..."
    )
)
async def classify_text_async(text: str, model: str, handler: CategoryHandler) -> Optional[str]:
    """Classify text using the external AI service."""
    labels = handler.get_labels()
    prompt_template = handler.get_prompt_template()
    
    prompt = prompt_template.format(
        text=text,
        labels=json.dumps(labels, ensure_ascii=False, indent=2)
    )
    
    payload = {
        "model": model,
        "messages": [{"role": "user", "content": prompt}]
    }

    response_data = await make_api_call(payload)
    content = response_data.get("choices", [{}])[0].get("message", {}).get("content", "")
    
    if not content:
        logger.error(f"No content returned from API for text: {text[:30]}...")
        raise ValueError("Empty response from API")

    try:
        result = json.loads(content)
        label = result.get("label")
        if label in labels:
            return label
        logger.warning(f"Invalid label returned for text '{text[:30]}...': {label}")
        raise ValueError(f"Invalid label: {label}")
    except json.JSONDecodeError as e:
        logger.error(f"JSON decode error for text '{text[:30]}...': {content}, error: {str(e)}")
        raise

# FastAPI endpoints
@app.post("/api/llm-classify", response_model=dict)
async def classify_endpoint(request: ClassificationRequest):
    """Classify text and return the label."""
    try:
        # Get category handler
        handler = category_registry.get_handler(request.category)
        if not handler:
            raise HTTPException(
                status_code=400, 
                detail=f"Invalid category: {request.category}. Available categories: {category_registry.get_available_categories()}"
            )
        
        # Extract text using handler
        text = handler.extract_text(request.data)
        
        # Check cache
        cache_key = generate_cache_key(request)
        if cache_key in cache:
            logger.info(f"Cache hit for text: {text[:100]}...")
            cached_label = cache[cache_key]
            return {
                "label": cached_label,
                "id": handler.get_label_ids()[cached_label]
            }

        # Classify text
        label = await classify_text_async(text, request.model, handler)
        if label is None:
            logger.error(f"Failed to classify text after {MAX_RETRIES} retries: {text[:100]}...")
            raise HTTPException(status_code=500, detail="Failed to classify text after retries")

        # Store in cache
        cache[cache_key] = label
        logger.info(f"Classified text '{text[:100]}...' as '{label}' for category '{request.category}'")
        
        return {
            "label": label,
            "id": handler.get_label_ids()[label]
        }

    except (ValueError, httpx.RequestError, httpx.HTTPStatusError) as e:
        logger.error(f"Error classifying text '{text[:30]}...': {str(e)}")
        raise HTTPException(status_code=500, detail=f"Classification error: {str(e)}")

@app.get("/api/categories")
async def get_categories():
    """Get available categories and their labels."""
    result = {}
    for category in category_registry.get_available_categories():
        handler = category_registry.get_handler(category)
        result[category] = {
            "labels": handler.get_labels(),
            "label_ids": handler.get_label_ids()
        }
    return result

@app.get("/api/categories/{category}")
async def get_category_info(category: str):
    """Get information about a specific category."""
    handler = category_registry.get_handler(category)
    if not handler:
        raise HTTPException(
            status_code=404,
            detail=f"Category not found: {category}. Available categories: {category_registry.get_available_categories()}"
        )
    
    return {
        "category": category,
        "labels": handler.get_labels(),
        "label_ids": handler.get_label_ids()
    }

# Health check endpoint
@app.get("/health")
async def health_check():
    """Health check endpoint."""
    return {
        "status": "healthy",
        "available_categories": category_registry.get_available_categories()
    }