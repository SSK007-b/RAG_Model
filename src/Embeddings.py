
from langchain_google_genai import GoogleGenerativeAIEmbeddings

class Embeddings:

    def __init__(self):
        pass

    def generate_embedding(text, key, model):
        """Generate embeddings for a given text."""
        embeddings = GoogleGenerativeAIEmbeddings(google_api_key=key, model=model)
        response = embeddings.embed_query(text)
        return response