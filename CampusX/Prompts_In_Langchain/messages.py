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

# Create a list of messages
messages = [

    # SystemMessage defines the AI's behavior
    SystemMessage(
        content="You are a helpful assistant."
    ),

    # HumanMessage represents the user's input
    HumanMessage(
        content="Tell me about LangChain"
    )
]

# Send all messages to the model
result = model.invoke(messages)

# Store the AI's response in the conversation history
messages.append(
    AIMessage(content=result.content)
)

# Print the complete conversation history
print(messages)