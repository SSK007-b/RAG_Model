# Document Extractor

The **Document Extractor** allows users to upload a PDF document, process its content, and ask questions based on the document's information. It uses **Google Generative AI** for generating embeddings and answering queries, and **FAISS** for efficient vector search.

## Features

- Upload PDF files.
- Extract the text from the PDF
- Generate embeddings for the text using **Google Generative AI**.
- Store embeddings in a FAISS index.
- Query the document and retrieve the most relevant sections.
- Generate AI-powered answers based on the retrieved content.

## Tech Stack

- **Python**
- **Streamlit** - For the user interface.
- **FAISS** - For efficient vector-based search.
- **Google Generative AI** - For embedding generation and answering queries.
- **PyPDF2** - For PDF text extraction.

---

## Installation

### Prerequisites

1. Python 3.8+
2. Google API Key for Generative AI
3. Libraries: `streamlit`, `faiss-cpu`, `langchain-google-genai`, `PyPDF2`, `python-dotenv`

### Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/SSK007-b/RAG_Model.git
   cd RAG_Model
   ```

3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the root directory and add your Google API key:
   ```
   GOOGLE_API=your_google_api_key
   ```

5. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```

---

## How to Use

1. **Upload a PDF File**:
   - Click on the file uploader and select a PDF document.

2. **Process the PDF**:
   - The system extracts and splits the text into smaller chunks.

3. **Generate and Store Embeddings**:
   - Click the "Generate and Store Embeddings" button to generate embeddings and save them in a FAISS index.

4. **Ask Questions**:
   - Enter a query related to the PDF content in the input box.
   - The system retrieves the top 5 relevant chunks and generates a meaningful answer.

---

## File Structure

```plaintext
.
├── app.py               # Main Streamlit app
├── requirements.txt     # List of Python dependencies
├── README.md            # Project documentation
├── .env                 # Environment variables
└── notebook/Data.pdf    # Example PDF file (optional)
```

---

## Dependencies

- `streamlit`: For building the user interface.
- `faiss-cpu`: For fast similarity search.
- `langchain-google-genai`: To interact with Google Generative AI.
- `PyPDF2`: For extracting text from PDFs.
- `python-dotenv`: To load environment variables.

Install them using:
```bash
pip install -r requirements.txt
```

---

## Future Improvements

- Add support for multiple file formats (e.g., Word, Text files).
- Enhance query accuracy by experimenting with different AI models.
- Add pagination and chunk visualization for better insights.

---

## License

This project is licensed under the [MIT License](LICENSE).

---

## Acknowledgments

- **Google Generative AI**: For powering embeddings and responses.
- **FAISS**: For fast and scalable vector search.
- **Streamlit**: For creating an interactive user interface.