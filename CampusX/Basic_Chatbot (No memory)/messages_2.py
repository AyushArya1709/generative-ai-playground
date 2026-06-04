from dotenv import load_dotenv
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_groq import ChatGroq

# Load API key from .env
load_dotenv()

# Initialize model
model = ChatGroq(
    model_name="llama-3.3-70b-versatile"
)

# Chat history starts with a system message
chat_history = [
    SystemMessage(
        content="You are a helpful assistant."
    )
]

while True:

    # Get user input
    user_input = input("You: ")

    # Exit condition
    if user_input.lower() in ["exit", "quit"]:
        print("Goodbye! 👋")
        break

    # Store user message
    chat_history.append(
        HumanMessage(content=user_input)
    )

    # Send complete conversation history to model
    response = model.invoke(chat_history)

    # Store AI response
    chat_history.append(
        AIMessage(content=response.content)
    )

    # Print AI response
    print(f"Chatbot: {response.content}")