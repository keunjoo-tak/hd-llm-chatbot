import os
from pathlib import Path

# 모델 리스트 정의
EMBEDDINGS_MODELS = [
    "BAAI/bge-base-en-v1.5",
    "sentence-transformers/all-MiniLM-L6-v2",
    "hkunlp/instructor-xl"
]

RERANKER_MODELS = [
    "ms-marco-MiniLM-L-12-v2",
    "cross-encoder/ms-marco-MiniLM-L-6-v2",
    "cross-encoder/mmarco-mMiniLMv2-L12-H384-v1"
]

LOCAL_LLM_MODELS = [
    "gemma2:9b",
    "llama2:7b",
    "mistral:7b"
]

REMOTE_LLM_MODELS = [
    "llama-3.1-70b-versatile",
    "gpt-4-turbo-preview",
    "claude-3-opus-20240229"
]

class Config:
    class Path:
        APP_HOME = Path(os.getenv("APP_HOME", Path(__file__).parent.parent))
        DATABASE_DIR = APP_HOME / "docs-db"
        DOCUMENTS_DIR = APP_HOME / "tmp"
        IMAGES_DIR = APP_HOME / "images"

    class Database:
        DOCUMENTS_COLLECTION = "documents"

    class Model:
        EMBEDDINGS = EMBEDDINGS_MODELS[0]
        RERANKER = RERANKER_MODELS[0]
        LOCAL_LLM = LOCAL_LLM_MODELS[0]
        REMOTE_LLM = REMOTE_LLM_MODELS[0]
        TEMPERATURE = 0.0
        MAX_TOKENS = 8000
        USE_LOCAL = False

    class Retriever:
        USE_RERANKER = True
        USE_CHAIN_FILTER = False

    DEBUG = False
    CONVERSATION_MESSAGES_LIMIT = 6