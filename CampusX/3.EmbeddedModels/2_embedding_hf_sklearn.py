from langchain_huggingface import HuggingFaceEmbeddings
from sklearn.metrics.pairwise import cosine_similarity

embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

documents = [
    "Delhi is the capital of India",
    "Kolkata is the capital of West Bengal",
    "Paris is the capital of France"
]

# Embed documents
vectors = embeddings.embed_documents(documents)

# Compute cosine similarity between the first document and the others
similarity = cosine_similarity([vectors[0]], vectors[1:])
print("Cosine Similarity:", similarity)

