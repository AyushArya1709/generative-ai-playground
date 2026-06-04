from langchain_groq import ChatGroq
from dotenv import load_dotenv
import streamlit as st
from langchain_core.prompts import load_prompt

# Load Environment Variables
load_dotenv()

# Initialize Groq Model
model = ChatGroq(
    model_name="llama-3.3-70b-versatile",
    temperature=0.3
)

# UI
st.set_page_config(page_title="Research Tool", page_icon="📚")

st.header("📚 Research Tool")

paper_input = st.selectbox(
    "Select Research Paper Name",
    [
        "Attention Is All You Need",
        "BERT: Pre-training of Deep Bidirectional Transformers",
        "GPT-3: Language Models are Few-Shot Learners",
        "Diffusion Models Beat GANs on Image Synthesis"
    ]
)

style_input = st.selectbox(
    "Select Explanation Style",
    [
        "Beginner-Friendly",
        "Technical",
        "Code-Oriented",
        "Mathematical"
    ]
)

length_input = st.selectbox(
    "Select Explanation Length",
    [
        "Short (1-2 paragraphs)",
        "Medium (3-5 paragraphs)",
        "Long (detailed explanation)"
    ]
)

# Load Prompt Template
template = load_prompt("template.json")

if st.button("Summarize"):

    chain = template | model

    with st.spinner("Generating Summary..."):
        result = chain.invoke(
            {
                "paper_input": paper_input,
                "style_input": style_input,
                "length_input": length_input
            }
        )

    st.write(result.content)