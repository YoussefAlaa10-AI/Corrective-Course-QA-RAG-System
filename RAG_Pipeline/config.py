import os
from pathlib import Path

# ==========================
# Project Paths
# ==========================
DATA_PATH = Path("DATA")
VECTOR_STORE_PATH = Path("vector_store")


# ==========================
# Chunking Settings
# ==========================
CHUNK_SIZE = 500
CHUNK_OVERLAP = 100


# ==========================
# Embedding Model
# ==========================
EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"


# ==========================
# Retriever Settings
# ==========================
TOP_K = 3


# Corrective RAG Settings
RETRIEVAL_SCORE_THRESHOLD = 0.40
MAX_RETRIEVAL_ATTEMPTS = 2
ENABLE_QUERY_REWRITE = True


# ==========================
# Gemini
# ==========================
os.environ['GOOGLE_API_KEY'] = "Your Key"

LLM_MODEL = "gemini-flash-lite-latest"


# ==========================
# Hugging Face Cache
# ==========================
os.environ["HF_HOME"] = "./hf_cache"






