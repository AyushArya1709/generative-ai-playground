from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
import os

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="Qwen/Qwen3-4B-Instruct-2507",
    task="text-generation",
    provider="nscale",
    huggingfacehub_api_token=os.getenv("HF_TOKEN"),
    max_new_tokens=100
)

model = ChatHuggingFace(llm=llm)

result = model.invoke("What is the currency of India?")

print(result.content)