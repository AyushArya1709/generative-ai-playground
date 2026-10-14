from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_groq import ChatGroq

# Load environment variables from .env
# (e.g. GROQ_API_KEY)
load_dotenv()

# Initialize the Groq model
model = ChatGroq(
    model_name="llama-3.3-70b-versatile"
)

# Create a prompt template
# {name} is a placeholder that will be replaced later

template = PromptTemplate(
    template="""
Greet this person in 5 languages.
The name of the person is {name}
""",
    input_variables=["name"]
)

# Fill the placeholder with an actual value
# This creates a PromptValue object

prompt = template.invoke(
    {"name": "Nitish"}
)

# Send the completed prompt to the model
result = model.invoke(prompt)

# Print the model's response
print(result.content)