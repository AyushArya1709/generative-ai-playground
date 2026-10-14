from dotenv import load_dotenv
from langchain_groq import ChatGroq

# Load environment variables from .env
# (e.g. GROQ_API_KEY)
load_dotenv()

# Initialize the Groq model
#
# temperature controls creativity:
# 0.0 = very deterministic
# 1.0 = balanced
# >1.0 = more creative/random
model = ChatGroq(
    model_name="llama-3.3-70b-versatile",
    temperature=1.5
)

# Send a prompt to the model
result = model.invoke(
    "Write a 5 line poem on cricket"
)

# Print the model's response
print(result.content)