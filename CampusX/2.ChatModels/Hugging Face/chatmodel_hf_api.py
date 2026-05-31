import os

from dotenv import load_dotenv
from langchain_huggingface import (
    HuggingFaceEndpoint,
    ChatHuggingFace
)

# Load environment variables
load_dotenv()

# Create Hugging Face endpoint
endpoint = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct",
    task="text-generation",
    huggingfacehub_api_token=os.getenv("HUGGINGFACEHUB_API_TOKEN")
)

# Create chat model
chatbot = ChatHuggingFace(llm=endpoint)

# Generate response
response = chatbot.invoke("What is the capital of India?")

# Print output
print(response.content)