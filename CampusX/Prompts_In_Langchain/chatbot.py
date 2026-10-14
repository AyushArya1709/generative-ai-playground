from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

# Load environment variables from .env
# (e.g. GROQ_API_KEY)
load_dotenv()

# Initialize the Groq model
model = ChatGroq(
    model_name="llama-3.3-70b-versatile"
)

# Chat history stores the entire conversation
# Start with a SystemMessage that defines the AI's behavior
chat_history = [
    SystemMessage(
        content="You are a helpful AI assistant."
    )
]

while True:

    # Get input from the user
    user_input = input("You: ")

    # Exit condition
    if user_input.lower() == "exit":
        break

    # Store the user's message in chat history
    chat_history.append(
        HumanMessage(content=user_input)
    )

    # Send the COMPLETE conversation history
    # to the model
    result = model.invoke(chat_history)

    # Store the AI's response in chat history
    # so the model can "remember" it later
    chat_history.append(
        AIMessage(content=result.content)
    )

    # Display the AI's response
    print("AI:", result.content)

# Print the complete conversation after exiting
print(chat_history)