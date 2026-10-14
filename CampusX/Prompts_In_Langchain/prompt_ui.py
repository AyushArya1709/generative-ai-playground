from dotenv import load_dotenv
import streamlit as st

from langchain_groq import ChatGroq
from langchain_core.prompts import load_prompt

# Load environment variables from .env
# (e.g. GROQ_API_KEY)
load_dotenv()

# Initialize the Groq model
model = ChatGroq(
    model_name="llama-3.3-70b-versatile"
)

# Streamlit page title
st.header("Research Tool")

# Dropdown to select the research paper
paper_input = st.selectbox(
    "Select Research Paper Name",
    [
        "Attention Is All You Need",
        "BERT: Pre-training of Deep Bidirectional Transformers",
        "GPT-3: Language Models are Few-Shot Learners",
        "Diffusion Models Beat GANs on Image Synthesis"
    ]
)

# Dropdown to select explanation style
style_input = st.selectbox(
    "Select Explanation Style",
    [
        "Beginner-Friendly",
        "Technical",
        "Code-Oriented",
        "Mathematical"
    ]
)

# Dropdown to select explanation length
length_input = st.selectbox(
    "Select Explanation Length",
    [
        "Short (1-2 paragraphs)",
        "Medium (3-5 paragraphs)",
        "Long (detailed explanation)"
    ]
)

# Load the prompt template from template.json
template = load_prompt("template.json")

# Execute when button is clicked
if st.button("Summarize"):

    # Create a chain:
    # PromptTemplate → Model
    chain = template | model

    # Fill the placeholders and send the prompt
    # to the model
    result = chain.invoke(
        {
            "paper_input": paper_input,
            "style_input": style_input,
            "length_input": length_input
        }
    )

    # Display the model's response
    st.write(result.content)