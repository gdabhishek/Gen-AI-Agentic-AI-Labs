"""
Configuration file for Customer Support Chatbot with RAG
"""
import os
from dotenv import load_dotenv

load_dotenv()

# Qdrant Cloud Configuration
QDRANT_URL = os.getenv("QDRANT_URL", "https://your-cluster-id.qdrant.io")
QDRANT_API_KEY = os.getenv("QDRANT_API_KEY", "your-api-key-here")
QDRANT_COLLECTION_NAME = "solarnova_customer_support"


# OpenAI Embeddings Configuration
EMBEDDING_MODEL = "text-embedding-3-small"
EMBEDDING_DIMENSIONS = 1536

# LLM Configuration
LLM_MODEL = "claude-sonnet-4-20250514"
LLM_PROVIDER = "anthropic"
LLM_BASE_URL = None

# Document Processing Configuration
PDF_PATH = "data/SolarNova Dynamics - Business Document.pdf"
CHUNK_SIZE = 1000
CHUNK_OVERLAP = 200

# Retrieval Configuration
RETRIEVAL_K = 3  # Number of chunks to retrieve

# Chat History Configuration
CHAT_DB_PATH = "customer_support_conversations.db"

