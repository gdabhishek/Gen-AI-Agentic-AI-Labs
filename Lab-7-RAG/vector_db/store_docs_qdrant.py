from langchain_qdrant import Qdrant
from langchain_openai import OpenAIEmbeddings
from langchain_core.documents import Document
import os
from dotenv import load_dotenv
from qdrant_client.http.models import Distance, VectorParams
load_dotenv()

# Initialize embeddings
embeddings = OpenAIEmbeddings(model = "text-embedding-3-small") #1536 dimensions

# Sample documents
# Sample documents
documents = [
    Document(
        page_content="Machine learning algorithms require large datasets for training.",
        metadata={"topic": "machine_learning", "category": "AI", "type": "training"}
    ),
    Document(
        page_content="Deep learning uses neural networks with multiple layers.",
        metadata={"topic": "deep_learning", "category": "AI", "type": "architecture"}
    ),
    Document(
        page_content="Natural language processing helps computers understand human language.",
        metadata={"topic": "NLP", "category": "AI", "type": "application"}
    ),
    Document(
        page_content="Computer vision enables machines to interpret visual information.",
        metadata={"topic": "computer_vision", "category": "AI", "type": "application"}
    )
]

# Qdrant Cloud vector store
# Replace with your Qdrant Cloud URL and API key
# You can get these from https://cloud.qdrant.io/
# Ensure your Qdrant Cloud URL and API key are set in a .env file as follows:
# QDRANT_URL=https://your-cluster-id.qdrant.io
# QDRANT_API_KEY=your-api-key-here

from qdrant_client import QdrantClient

# Create Qdrant client for Cloud
client = QdrantClient(
    url=os.getenv("QDRANT_URL", "https://your-cluster-id.qdrant.io"),
    api_key=os.getenv("QDRANT_API_KEY", "your-api-key-here"),
)
client.create_collection(
    collection_name="test_collection",
    vectors_config=VectorParams(size=1536, distance=Distance.COSINE),
)
# Initialize Qdrant vector store with client and embeddings
vector_store = Qdrant(
    client=client,
    collection_name="test_collection",
    embeddings=embeddings,
)

# Add documents to the vector store
vector_store.add_documents(documents)

# For local Qdrant, use this instead:
# from qdrant_client import QdrantClient
# client = QdrantClient(path="./qdrant_db")  # Local path for Qdrant storage
# vector_store = Qdrant(
#     client=client,
#     collection_name="example_collection",
#     embeddings=embeddings,
# )
# vector_store.add_documents(documents)

