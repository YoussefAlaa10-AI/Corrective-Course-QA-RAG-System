from RAG_Pipeline.config import EMBEDDING_MODEL ,TOP_K, VECTOR_STORE_PATH
from sentence_transformers import SentenceTransformer
import faiss
import os ,pickle
import numpy as np


# Load Embedding Model
embedding_model = SentenceTransformer(EMBEDDING_MODEL)


# Load FAISS Index
index = faiss.read_index(os.path.join(VECTOR_STORE_PATH, "faiss.index"))

# Load Chunks
with open(os.path.join(VECTOR_STORE_PATH, "chunks.pkl"),"rb") as file:
    chunks = pickle.load(file)



def retrieve(query):

    """
    Retrieve the most relevant chunks for a user query.
    """
    # Convert query to embedding
    query_embedding = embedding_model.encode([query])

    query_embedding = np.array(query_embedding,dtype=np.float32)

    # Search in FAISS
    dis , indices = index.search(query_embedding,TOP_K)

    results = []

    for idx in indices[0]:
        results.append(
            chunks[idx]
        )

    return results    





