from langchain_groq import ChatGroq
from langchain_core.prompts import load_prompt
from pypdf import PdfReader
from dotenv import load_dotenv
import streamlit as st


load_dotenv()

# LLM
llm = ChatGroq(
    model_name="llama-3.1-8b-instant"
)

# Prompt Template
template = load_prompt("template.json")

# UI
st.title("📚 Research Paper Explainer")

uploaded_file = st.file_uploader(
    "Upload Research Paper (PDF)",
    type="pdf"
)

style_input = st.selectbox(
    "Explanation Style",
    [
        "Beginner-Friendly",
        "Technical",
        "Code-Oriented",
        "Mathematical"
    ]
)

length_input = st.selectbox(
    "Explanation Length",
    [
        "Short",
        "Medium",
        "Long"
    ]
)

if st.button("Summarize"):

    if uploaded_file is None:
        st.warning("Please upload a PDF.")
        st.stop()

    # Extract PDF Text
    paper_text = ""

    pdf_reader = PdfReader(uploaded_file)

    for page in pdf_reader.pages:
        text = page.extract_text()

        if text:
            paper_text += text

    # Create Chain
    chain = template | llm

    response = chain.invoke({
        "paper_input": paper_text,
        "style_input": style_input,
        "length_input": length_input
    })

    st.subheader("Summary")

    st.write(response.content)