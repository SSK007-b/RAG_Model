import faiss
import numpy as np
from .Embeddings import Embeddings
from dotenv import load_dotenv
import os

load_dotenv()

class VectorStore:
    def __init__(self):
        pass

    def store_embeddings(embeddings, index_path="vectors.index"):
        embeddings_array = np.array(embeddings, dtype='float32')

        if embeddings_array.ndim == 1:
            embeddings_array = np.expand_dims(embeddings_array, axis=0)

        dimension = embeddings_array.shape[1]

        index = faiss.IndexFlatL2(dimension)
        index.add(embeddings_array)
        faiss.write_index(index, index_path)
        print(f"FAISS index stored locally at {index_path}.")

    def retrieve_document_from_faiss(query, index_path="vectors.index", documents=None):

        index = faiss.read_index(index_path)
        query_embedding = Embeddings.generate_embedding(query, key=os.getenv("GOOGLE_API"), model='models/embedding-001')

        query_embedding = np.array(query_embedding, dtype='float32').reshape(1, -1)

        indices = index.search(query_embedding, 1)

        print(indices[0][0][0])
        return documents[int(indices[0][0][0])]