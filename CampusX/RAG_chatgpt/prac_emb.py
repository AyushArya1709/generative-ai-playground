from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)

chunks = [
    "Transformers use self-attention mechanisms.",
    "Cats are small domestic animals.",
    "Machine learning is a subset of AI."
]

embeddings = model.encode(chunks)

print(embeddings[0])

print(len(embeddings[0]))

print(embeddings.shape)

question = "What are transformers?"

question_embedding = model.encode(question)

print(len(question_embedding))
print(question_embedding.shape)