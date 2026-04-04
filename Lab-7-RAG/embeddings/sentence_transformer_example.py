

from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
from visualization_utils import visualize_embeddings_3d
import numpy as np

# Load pre-trained embedding model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Create embeddings
texts = [
    "Machine learning algorithms",
    "Deep learning neural networks", 
    "Natural language processing",
    "Computer vision applications",
    "Data science techniques",
    "I love coffee"
]

# Convert text into embedding vectors
embeddings = model.encode(texts)

print("Embeddings shape:", embeddings.shape)
print("\nEmbeddings (first few values):")
print(embeddings[0][:10], "...")  # Print first 10 values of first embedding

# Calculate similarities using cosine similarity
similarities = cosine_similarity(embeddings)

print("\nSimilarity Matrix:")
print(similarities)

print("\nSentence Similarities:")
for i, text1 in enumerate(texts):
    for j, text2 in enumerate(texts):
        if i < j:
            print(f"'{text1}' vs '{text2}': {similarities[i][j]:.3f}")

# Visualize embeddings in 3D
visualize_embeddings_3d(embeddings, texts, title="SentenceTransformer Embeddings - 3D Visualization")

