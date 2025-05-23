from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import httpx
import json
from cachetools import LRUCache
import logging
from tenacity import retry, stop_after_attempt, wait_fixed, retry_if_exception_type
from typing import Optional
import hashlib
import os

# Load environment variables from .env file
from dotenv import load_dotenv
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

# Label IDs
LABEL_IDS = {
    "Ad sales": "675aa336e751a10ea07e70cf",
    "Brand mention": "5f473b1e5966faeb2259f5e4",
    "Counters/ Telesales": "5f473b0c5966faeb2259f5e3",
    "Debt Issues": "5f40d1cebc260e60500c2b86",
    "Fee/ Charge": "6088d05092f9ed4ad71d874a",
    "Harassment for Collection": "5f40d1f1bc260e60500c2b89",
    "Harassment for Non Client": "5f40d1d8bc260e60500c2b87",
    "Harassment for Selling": "5f40d1e3bc260e60500c2b88",
    "Harassment on Client's Relative": "60e7b3cddbc2292f90771652",
    "Interest": "6088d04692f9ed4ad71d8749",
    "Mobile app": "5f473ceba2d624f9dc50abfd",
    "Process/ Procedure": "675a88cde751a10ea07e70bd",
    "Product information": "675a88c7e751a10ea07e70bc",
    "Recruitment/ Training": "5f211c807e6e09dd8343b720",
    "Sellers/ Consultant": "5f473af05966faeb2259f5de",
    "Terminate procedure": "675aa2e4e751a10ea07e70ce",
    "General mention": "5f40cdd7bc260e60500c2af0",
    "Staff attitude": "5f40ce02bc260e60500c2af1",
    "Minigame/ livestream": "62cce32b33161b492fad9fcd",
    "ESG (Environmental Social Governance)": "675a8910e751a10ea07e70c4",
    "Promotion/ campaign": "675a88d5e751a10ea07e70be",
    "Achievement": "682ee20f64598918c0f46f26",
    "Business result": "682ee22364598918c0f46f27",
    "Interactive posts": "682ee22864598918c0f46f28"
}

# Label definitions
LABELS = {
    "Ad sales": "Nội dung quảng bá bán hàng, lời kêu gọi mua sản phẩm/dịch vụ.",
    "Brand mention": "Nội dung chỉ đơn thuần đề cập đến thương hiệu, không có cảm xúc rõ ràng hay ý định cụ thể.",
    "Counters/ Telesales": "Nội dung phản ánh về nhân viên tại quầy, telesales: gọi điện mời chào, tư vấn sản phẩm.",
    "Debt Issues": "Nội dung nói về việc nợ, trả nợ, chậm trả, khó khăn tài chính liên quan đến khoản vay.",
    "Fee/ Charge": "Phàn nàn, câu hỏi, hoặc thông tin liên quan đến phí dịch vụ, các khoản thu thêm.",
    "Harassment for Collection": "Phản ánh việc bị làm phiền do thu hồi nợ: gọi điện, nhắn tin, đe dọa.",
    "Harassment for Non Client": "Phản ánh bị làm phiền dù không phải khách hàng (gọi nhầm, spam).",
    "Harassment for Selling": "Phản ánh bị làm phiền vì mục đích bán hàng (quảng cáo, tiếp thị qua điện thoại).",
    "Harassment on Client's Relative": "Phản ánh việc làm phiền người thân của khách hàng về nợ, bán hàng, liên hệ gián tiếp.",
    "Interest": "Nội dung nói về lãi suất: cao, thấp, thay đổi, câu hỏi về mức lãi.",
    "Mobile app": "Đánh giá, phản ánh, hướng dẫn hoặc lỗi liên quan đến ứng dụng di động.",
    "Process/ Procedure": "Nội dung đề cập đến quy trình, thủ tục: mở tài khoản, vay vốn, thanh lý, v.v.",
    "Product information": "Câu hỏi, chia sẻ, mô tả về sản phẩm/dịch vụ đang được cung cấp.",
    "Recruitment/ Training": "Nội dung về tuyển dụng, đào tạo nhân viên, phỏng vấn, chia sẻ kinh nghiệm làm việc.",
    "Sellers/ Consultant": "Nội dung liên quan đến người bán hàng, tư vấn viên: thái độ, kiến thức, chăm sóc khách hàng.",
    "Terminate procedure": "Phản ánh hoặc hỏi về thủ tục chấm dứt dịch vụ, kết thúc hợp đồng, tất toán, đóng tài khoản.",
    "General mention": "Đề cập tổng quan về thương hiệu, không rõ vấn đề cụ thể.",
    "Staff attitude": "Nội dung nhận xét thái độ nhân viên: thân thiện, thô lỗ, hỗ trợ tốt/kém.",
    "Minigame/ livestream": "Nội dung liên quan đến mini game, livestream trên mạng xã hội hoặc kênh truyền thông.",
    "ESG": "Nội dung liên quan đến môi trường, xã hội, quản trị doanh nghiệp – ví dụ như hoạt động CSR.",
    "Promotion/ campaign": "Chia sẻ, thắc mắc hoặc phản ánh về chương trình khuyến mãi, ưu đãi, giảm giá.",
    "Achievement": "Nội dung ca ngợi, nêu thành tích thương hiệu (giải thưởng, xếp hạng, mốc tăng trưởng).",
    "Business result": "Thông tin, phân tích, báo cáo kết quả kinh doanh, doanh thu, lợi nhuận.",
    "Interactive posts": "Nội dung tương tác với người dùng: câu hỏi, bình chọn, trò chơi, lời kêu gọi tham gia hoạt động."
}

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
async def classify_text_async(text: str, model: str) -> Optional[str]:
    """Classify text using the external AI service."""
    prompt = f"""Bạn là một trợ lý phân loại nội dung trong lĩnh vực tài chính, ngữ cảnh social listening. 
Dựa trên văn bản sau, hãy chọn **một nhãn duy nhất** phù hợp nhất từ danh sách nhãn được cung cấp. 
Trả về **chỉ nhãn** dưới dạng chuỗi JSON, ví dụ: {{"label": "Ad sales"}}.

**Văn bản**: {text}

**Danh sách nhãn và mô tả**:
{json.dumps(LABELS, ensure_ascii=False, indent=2)}
"""
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
        if label in LABELS:
            return label
        logger.warning(f"Invalid label returned for text '{text[:30]}...': {label}")
        raise ValueError(f"Invalid label: {label}")
    except json.JSONDecodeError as e:
        logger.error(f"JSON decode error for text '{text[:30]}...': {content}, error: {str(e)}")
        raise

# FastAPI endpoint
@app.post("/api/llm-classify", response_model=dict)
async def classify_endpoint(request: ClassificationRequest):
    """Classify text and return the label."""
    try:
        # merge text
        text = request.data.get("title", "") + " " + request.data.get("content", "") + " " + request.data.get("description", "")
        if request.category == "finance":
            # Check cache
            cache_key = generate_cache_key(request)
            if cache_key in cache:
                logger.info(f"Cache hit for text: {text[:100]}...")
                return {
                    "label": cache[cache_key],
                    "id": LABEL_IDS[cache[cache_key]]}

            # Classify text
            label = await classify_text_async(text, request.model)
            if label is None:
                logger.error(f"Failed to classify text after {MAX_RETRIES} retries: {text[:100]}...")
                raise HTTPException(status_code=500, detail="Failed to classify text after retries")

            # Store in cache
            cache[cache_key] = label
            logger.info(f"Classified text '{text[:100]}...' as '{label}'")
            return {
                "label": label,
                "id": LABEL_IDS[label]
            }

        else:
            raise HTTPException(status_code=400, detail="Invalid category")

    except (ValueError, httpx.RequestError, httpx.HTTPStatusError) as e:
        logger.error(f"Error classifying text '{text[:30]}...': {str(e)}")
        raise HTTPException(status_code=500, detail=f"Classification error: {str(e)}")

# Health check endpoint
@app.get("/health")
async def health_check():
    """Health check endpoint."""
    return {"status": "healthy"}