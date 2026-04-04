from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
load_dotenv()
embeddings = OpenAIEmbeddings(model = "text-embedding-3-small")

vector_store = Chroma(
    collection_name="test_collection_cosine",
    embedding_function=embeddings,
    persist_directory="./chroma_langchain_db",
)


# Query the vector store
query = "What is machine learning?"
#k -- no of results to return
results = vector_store.similarity_search(query, k=2) # k is the number of docs to return based on the similarity score

print("Chroma Results:")
print(results)
print("\n" + "="*50 + "\n")
results_with_score = vector_store.similarity_search_with_score(query, k=2)
print("Chroma Results with score:")
print(results_with_score)

