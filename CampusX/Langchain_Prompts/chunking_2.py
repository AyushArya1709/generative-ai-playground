from langchain_groq import ChatGroq
from langchain_core.prompts import load_prompt
from langchain_text_splitters import RecursiveCharacterTextSplitter
from pypdf import PdfReader
from dotenv import load_dotenv
import streamlit as st

# -------------------------
# Setup
# -------------------------

load_dotenv()

llm = ChatGroq(
    model_name="llama-3.1-8b-instant"
)

template = load_prompt("template.json")

# -------------------------
# UI
# -------------------------

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

# -------------------------
# Main Logic
# -------------------------

if st.button("Summarize"):

    if uploaded_file is None:
        st.warning("Please upload a PDF.")
        st.stop()

    # -------------------------
    # Extract PDF Text
    # -------------------------

    paper_text = ""

    pdf_reader = PdfReader(uploaded_file)

    for page in pdf_reader.pages:

        text = page.extract_text()

        if text:
            paper_text += text

    # -------------------------
    # Chunking
    # -------------------------

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )

    chunks = splitter.split_text(paper_text)

    st.success("Chunking completed!")

    st.write(f"Total Chunks: {len(chunks)}")

    # -------------------------
    # Show First Chunk
    # -------------------------

    st.subheader("First Chunk")

    st.write(chunks[0])

    # -------------------------
    # LLM Summary
    # -------------------------

    chain = template | llm

    response = chain.invoke({
        "paper_input": chunks[0],   # <-- IMPORTANT
        "style_input": style_input,
        "length_input": length_input
    })

    st.subheader("Summary of First Chunk")

    st.write(response.content)