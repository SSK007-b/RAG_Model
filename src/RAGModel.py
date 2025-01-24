from langchain_google_genai import ChatGoogleGenerativeAI
import os
from dotenv import load_dotenv

load_dotenv()

class Model:
    def __init__(self):
        pass

    def generate_response(query, retrieved_data, google_api_key=None, model_name="gemini-1.5-flash"):
        """Generate a response based on the retrieved data."""
        if not google_api_key:
            google_api_key = os.getenv("GOOGLE_API")
    
        if not google_api_key:
            raise ValueError("Google API key is required and should be set in environment variables.")
    
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