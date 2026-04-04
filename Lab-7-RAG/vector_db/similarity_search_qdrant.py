from langchain_qdrant import QdrantVectorStore, RetrievalMode
from langchain_openai import OpenAIEmbeddings
import os
from dotenv import load_dotenv
load_dotenv()

embeddings = OpenAIEmbeddings(model = "text-embedding-3-small")


from qdrant_client import QdrantClient
client = QdrantClient(
    url=os.getenv("QDRANT_URL", "https://your-cluster-id.qdrant.io"),
    api_key=os.getenv("QDRANT_API_KEY", "your-api-key-here"),
)
vector_store = QdrantVectorStore(
    client=client,
    collection_name="test_collection",
    embedding=embeddings,
    retrieval_mode=RetrievalMode.DENSE,
)

# For local Qdrant, use this instead:
# vector_store = Qdrant.from_existing_collection(
#     embedding=embeddings,
#     path="./qdrant_db",  # Local path for Qdrant storage
#     collection_name="test_collection",
# )


# Query the vector store
query = "What is machine learning?"
#k -- no of results to return
results = vector_store.similarity_search(query, k=2)

print("Qdrant Results:")
print(results)

print("\n" + "="*50 + "\n")
print("Qdrant Results with score:")
results_with_score = vector_store.similarity_search_with_score(query, k=2)

print(results_with_score)



