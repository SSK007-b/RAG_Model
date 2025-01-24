import os
import numpy as np
import faiss
import streamlit as st
from PyPDF2 import PdfReader
from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()
key = os.getenv("GOOGLE_API")
model = "models/embedding-001"

def read_pdf(file):
    """Extract text from uploaded PDF."""
    text = ""
    reader = PdfReader(file)
    for i in range(len(reader.pages)):
        page = reader.pages[i]
        text += page.extract_text()
    return str(text)

def split_into_chunks(text, chunk_size=500):
    """Split text into smaller chunks."""
    words = text.split()
    chunks = [' '.join(words[i:i + chunk_size]) for i in range(0, len(words), chunk_size)]
    return chunks

def generate_embedding(text, key, model):
    """Generate embeddings for the text."""
    embeddings = GoogleGenerativeAIEmbeddings(google_api_key=key, model=model)
    response = embeddings.embed_query(text)
    return response

def store_embeddings(chunks, key, model, index_path="vectors.index"):
    """Store embeddings for chunks in FAISS."""
    embeddings_list = []
    for chunk in chunks:
        embedding = generate_embedding(chunk, key, model)
        embeddings_list.append(embedding)
    
    embeddings_array = np.array(embeddings_list, dtype='float32')
    dimension = embeddings_array.shape[1]

    index = faiss.IndexFlatL2(dimension)
    index.add(embeddings_array)
    faiss.write_index(index, index_path)
    return f"FAISS index stored at {index_path}"

def retrieve_top_chunks(query, key, model, index_path="vectors.index", chunks=None, top_k=5):
    """Retrieve top-k relevant chunks."""
    index = faiss.read_index(index_path)
    query_embedding = generate_embedding(query, key, model)
    query_embedding = np.array(query_embedding, dtype='float32').reshape(1, -1)
    
    distances, indices = index.search(query_embedding, top_k)
    top_chunks = [chunks[i] for i in indices[0] if i < len(chunks)]
    return top_chunks

def generate_response(query, retrieved_data, google_api_key=None, model_name="gemini-1.5-flash"):
    """Generate response from retrieved chunks."""
    if not google_api_key:
        google_api_key = os.getenv("GOOGLE_API")
    if not google_api_key:
        raise ValueError("Google API key is required.")

    prompt = (
        f"Context:\n{retrieved_data}\n\n"
        f"Question: {query}\n"
        f"Answer:"
    )
    try:
        model = ChatGoogleGenerativeAI(google_api_key=google_api_key, model=model_name)
        response = model.invoke(prompt)
        return response.content
    except Exception as e:
        raise RuntimeError(f"Error generating response: {e}")

# Streamlit UI
