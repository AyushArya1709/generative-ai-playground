from dotenv import load_dotenv
from langchain_core.messages import SystemMessage, HumanMessage
from langchain_groq import ChatGroq

# Load environment variables from .env file
load_dotenv()

# Initialize the Groq model
model = ChatGroq(
    model_name="llama-3.3-70b-versatile"
)

# System instruction for the AI
system_message = SystemMessage(
    content="You are a helpful assistant."
)

# User message
human_message = HumanMessage(
    content="Hello, how are you?"
)

# Send messages to the model
response = model.invoke([
    system_message,
    human_message
])

# Print the AI response
print("Chatbot:", response.content)