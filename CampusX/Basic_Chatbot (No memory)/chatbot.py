from dotenv import load_dotenv
from langchain_groq import ChatGroq

# Load environment variables from .env file
load_dotenv()

# Initialize the Groq model
model = ChatGroq(
    model_name="llama-3.3-70b-versatile"
)

# List that stores the complete conversation
chat_history = []

while True:

    # Take input from user
    user_input = input("You: ")

    # Exit condition
    if user_input.lower() in ["exit", "quit"]:
        print("Exiting the chatbot. Goodbye!")
        break

    # Create a tuple:
    # ("user", actual_message)
    #
    # Example:
    # ("user", "Hello")
    #
    # and store it in chat history
    chat_history.append(
        ("user", user_input)
    )

    # Convert chat history into a string
    # because the model cannot understand Python tuples directly
    formatted_history = ""

    for role, message in chat_history:
        formatted_history += f"{role.capitalize()}: {message}\n"

    # Send the entire conversation to the model
    # This gives the illusion of memory
    response = model.invoke(formatted_history)

    # Store AI response as a tuple
    #
    # Example:
    # ("assistant", "Hi Ayush!")
    #
    chat_history.append(
        ("assistant", response.content)
    )

    # Display response
    print(f"Chatbot: {response.content}")

# ------------------------------------
# Print complete chat history
# ------------------------------------

print("\nChat History:")

for role, message in chat_history:

    # Example:
    # role = "user"
    # message = "Hello"

    print(f"{role.capitalize()}: {message}")