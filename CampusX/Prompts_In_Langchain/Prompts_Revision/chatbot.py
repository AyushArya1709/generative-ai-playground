from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
import os

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="Qwen/Qwen3-4B-Instruct-2507",
    task="text-generation",
    provider="nscale",
    huggingfacehub_api_token=os.getenv("HF_TOKEN"),
)

model = ChatHuggingFace(llm=llm)

chat_history = []

"""
result = model.invoke("What is the currency of India?")

print(result.content) """

while True:
    user_input = input("User: ")
    chat_history.append({"role": "user", "content": user_input})
    if user_input.lower() in ["exit", "quit"]:
        print("Exiting the chatbot. Goodbye!")
        break                                       

    result = model.invoke(user_input)
    print(f"Bot: {result.content}")
    
print(chat_history)