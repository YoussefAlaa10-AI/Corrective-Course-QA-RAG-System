import faiss
from RAG_Pipeline.config import VECTOR_STORE_PATH
import pickle
import numpy as np
import os

def create_vector_database(chunk_documents,embedding):

    """
    Create a FAISS vector database and save chunk metadata.
    """
    # Convert embeddings to NumPy array
    embedding = np.array(embedding,dtype=np.float32)

    # Create FAISS index
    index = faiss.IndexFlatL2(embedding.shape[1])

    # Add embeddings to the index
    index.add(embedding)

    # Create vector store folder
    os.makedirs(VECTOR_STORE_PATH,exist_ok=True)

    # Save FAISS index
    faiss.write_index(index,os.path.join(VECTOR_STORE_PATH,"faiss.index"))

    # Save chunks and metadata
    with open(os.path.join(VECTOR_STORE_PATH,"chunks.pkl"),"wb") as file:
        pickle.dump(chunk_documents, file)

    print("Vector Database Created Successfully!")     

















