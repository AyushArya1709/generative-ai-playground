from langchain_huggingface import (
    HuggingFacePipeline,
    ChatHuggingFace
)

# Load local model
pipeline = HuggingFacePipeline.from_model_id(
    model_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation",

    pipeline_kwargs={
        "temperature": 0.7,
        "max_new_tokens": 128,
        "do_sample": True,
        "return_full_text": False
    }
)

# Convert into chat model
chatbot = ChatHuggingFace(llm=pipeline)

print("Local AI Chat Started 😭\n")

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Goodbye!")
        break

    response = chatbot.invoke(user_input)

    print("AI:", response.content)