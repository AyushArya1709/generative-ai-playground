from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# -----------------------------
# 1. Load Embedding Model
# -----------------------------

model = SentenceTransformer("all-MiniLM-L6-v2")

# -----------------------------
# 2. Create Chunks
# -----------------------------

chunks = [
    "Transformers use self-attention mechanisms.",
    "Cats are small domestic animals.",
    "Machine learning is a subset of AI."
]

# -----------------------------
# 3. Convert Chunks to Embeddings
# -----------------------------

chunk_embeddings = model.encode(chunks)

print("Chunk Embeddings Shape:")
print(chunk_embeddings.shape)

# -----------------------------
# 4. User Question
# -----------------------------

question = "What are transformers?"

# -----------------------------
# 5. Convert Question to Embedding
# -----------------------------

question_embedding = model.encode(question)

print("\nQuestion Embedding Shape:")
print(question_embedding.shape)

# -----------------------------
# 6. Compare Question with Chunks
# -----------------------------

similarity_scores = cosine_similarity(
    [question_embedding],
    chunk_embeddings
)

# -----------------------------
# 7. Raw Similarity Scores
# -----------------------------

print("\nRaw Similarity Scores:")
print(similarity_scores)

# -----------------------------
# 8. Human Readable Scores
# -----------------------------

print("\nSimilarity Scores:")

for chunk, score in zip(chunks, similarity_scores[0]):
    print(f"{score:.4f} -> {chunk}")

# -----------------------------
# 9. Rank Chunks
# -----------------------------

sorted_indices = np.argsort(
    similarity_scores[0]
)[::-1]

print("\n=== Ranked Chunks ===")

for rank, idx in enumerate(sorted_indices, start=1):
    print(
        f"Rank {rank} | Score: {similarity_scores[0][idx]:.4f}"
    )
    print(chunks[idx])
    print("-" * 50)

# -----------------------------
# 10. Retrieve Top-K Chunks
# -----------------------------

top_k = 2

retrieved_chunks = [
    chunks[idx]
    for idx in sorted_indices[:top_k]
]

print(f"\n=== Top {top_k} Retrieved Chunks ===")

for chunk in retrieved_chunks:
    print(chunk)
    print("-" * 50)

# -----------------------------
# 11. Final Context
# -----------------------------

context = "\n\n".join(retrieved_chunks)

print("\n=== Context Sent to LLM ===")
print(context)