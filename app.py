import streamlit as st
from src.dataPreprocessing import Preprocessing
from src.RAGModel import Model
from src.Embeddings import Embeddings
from src.utils import VectorStore
from dotenv import load_dotenv
import os

load_dotenv()
key = os.getenv("GOOGLE_API")
model = "models/embedding-001"

st.title("AI PDF Query System")
st.write("Upload a PDF, and ask questions based on its content.")

# File uploader
uploaded_file = st.file_uploader("Upload your PDF", type=["pdf"])

if uploaded_file is not None:
    st.success("PDF uploaded successfully!")

    # Process the PDF
    with st.spinner("Processing the PDF..."):
        pdf_text = Preprocessing.read_pdf(uploaded_file)
        embeddings = Embeddings.generate_embedding(pdf_text, key, model)
    
    st.write("PDF has been split into chunks.")

    # Generate and store embeddings
    if st.button("Generate and Store Embeddings"):
        VectorStore.store_embeddings(embeddings)
        st.success("Embeddings generated and stored successfully!")

    # Query input
    query = st.text_input("Ask a question based on the PDF content:")
    if query:
        with st.spinner("Searching for answers..."):
            top_chunks = VectorStore.retrieve_document_from_faiss(query, documents=[pdf_text])
            combined_context = " ".join(top_chunks)
            response = Model.generate_response(query, combined_context)
        st.write("### Answer:")
        st.write(response)
