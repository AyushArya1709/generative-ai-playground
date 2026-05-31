from langchain_text_splitters import RecursiveCharacterTextSplitter
from pypdf import PdfReader
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

st.title("📚 Research Paper Chunking Demo")

uploaded_file = st.file_uploader(
    "Upload Research Paper (PDF)",
    type="pdf"
)

if st.button("Process PDF"):

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

    # Chunking

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )

    chunks = splitter.split_text(paper_text)

    st.success("Chunking completed!")

    st.write(f"Total Chunks: {len(chunks)}")

    # Show first chunk

    if len(chunks) > 0:
        st.subheader("Chunk 1")
        st.write(chunks[0])

    # Show second chunk

    if len(chunks) > 1:
        st.subheader("Chunk 2")
        st.write(chunks[1])