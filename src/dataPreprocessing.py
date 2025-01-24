from PyPDF2 import PdfReader
from langchain_google_genai import GoogleGenerativeAIEmbeddings


class Preprocessing:
    def __init__(self):
        pass
    
    def read_pdf(path):
        """Read PDF and extract text."""
        text = ""
        reader = PdfReader(path)
        for i in range(len(reader.pages)):
            page = reader.pages[i]
            text += page.extract_text()
        return str(text)