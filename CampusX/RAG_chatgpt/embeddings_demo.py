from sentence_transformers import SentenceTransformer

model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)

chunks = [
    "Transformers use self-attention mechanisms.",
    "Cats are small domestic animals.",
    "Machine learning is a subset of AI."
]

embeddings = model.encode(chunks)

print(embeddings.shape)

print(embeddings[0][:10])

question = "What are transformers?"

question_embedding = model.encode(question)

print(question_embedding.shape)