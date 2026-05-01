import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    
    GROQ_API_KEY = os.getenv("GROQ_API_KEY")
    if not GROQ_API_KEY:
        raise ValueError("Missing GROQ_API_KEY in .env file.")

    MONGO_URI = os.getenv("MONGO_URI")
    DEFAULT_DB_NAME = "sample_mflix"
    DEFAULT_COLLECTION_NAME = "movies"

    FLASK_HOST = "127.0.0.1"
    FLASK_PORT = 5000
    API_URL = f"http://{FLASK_HOST}:{FLASK_PORT}/ask"
    
    LLM_MODEL = "llama-3.1-8b-instant"