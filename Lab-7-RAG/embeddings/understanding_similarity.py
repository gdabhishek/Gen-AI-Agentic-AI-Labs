
import numpy as np

# Word vectors as points in space
king = np.array([0.2, 0.5, -0.1])
queen = np.array([0.3, 0.4, -0.2])
man = np.array([0.1, 0.3, 0.2])
woman = np.array([0.2, 0.2, 0.1])

# Semantic relationships
# print("King - Man + Woman ≈ Queen")
# result = king - man + woman
similarity = np.dot(king, woman) / (np.linalg.norm(king) * np.linalg.norm(woman))
print(f"Similarity king vs woman: {similarity:.3f}")
print(f"Similarity king vs man: {np.dot(king, man) / (np.linalg.norm(king) * np.linalg.norm(man)):.3f}")
print(f"Similarity queen vs woman: {np.dot(queen, woman) / (np.linalg.norm(queen) * np.linalg.norm(woman)):.3f}")
print(f"Similarity queen vs man: {np.dot(queen, man) / (np.linalg.norm(queen) * np.linalg.norm(man)):.3f}")