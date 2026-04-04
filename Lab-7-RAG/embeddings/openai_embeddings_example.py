
from langchain_openai import OpenAIEmbeddings
from visualization_utils import visualize_embeddings_3d
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
from dotenv import load_dotenv
import matplotlib.pyplot as plt
load_dotenv()

# Load OpenAI embedding model
model = OpenAIEmbeddings(model="text-embedding-3-small")

# Example texts
texts = [
    "Machine learning algorithms",
    "Deep learning neural networks", 
    "Natural language processing",
    "Computer vision applications",
    "Data science techniques"
]

# Create embeddings using OpenAI
tech_embeddings = model.embed_documents(texts) #1536

print(f"Number of texts: {len(texts)}")
print(f"Embedding dimensions: {len(tech_embeddings[0])}")

# Convert embeddings to numpy array for similarity calculation
embeddings_array = np.array(tech_embeddings)

# Calculate similarities using cosine similarity
similarities = cosine_similarity(embeddings_array)

print("\nSimilarity Matrix:")
print(similarities)

print("\nSentence Similarities:")
for i, text1 in enumerate(texts):
    for j, text2 in enumerate(texts):
        if i < j:
            print(f"'{text1}' vs '{text2}': {similarities[i][j]:.3f}")

# Visualize embeddings in 3D
visualize_embeddings_3d(tech_embeddings, texts, title="OpenAI Embeddings - 3D Visualization")

