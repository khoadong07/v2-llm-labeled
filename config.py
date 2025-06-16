import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    API_URL = os.getenv("API_URL")
    HEADERS = {"Content-Type": "application/json"}

    # Retry configuration
    MAX_RETRIES = 3
    RETRY_DELAY = 2