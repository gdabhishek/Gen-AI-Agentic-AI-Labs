from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings
from langchain_core.documents import Document
from dotenv import load_dotenv
load_dotenv()
# Initialize embeddings
embeddings = OpenAIEmbeddings(model = "text-embedding-3-small")

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

# Chroma vector store
vector_store = Chroma(
    collection_name="test_collection_cosine",
    embedding_function=embeddings,
    persist_directory="./chroma_langchain_db",
    collection_configuration={"hnsw": {"space": "cosine"}}
)

# Add documents to the vector store
vector_store.add_documents(documents)