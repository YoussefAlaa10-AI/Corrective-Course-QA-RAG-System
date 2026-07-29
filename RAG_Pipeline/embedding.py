from RAG_Pipeline.config import EMBEDDING_MODEL
from sentence_transformers import SentenceTransformer

embedding_model = SentenceTransformer(EMBEDDING_MODEL)


def create_embeddings(chunks):

    """
    Convert text chunks into vector embeddings.
    """
    texts = []

    for chunk in chunks:
        texts.append(chunk["chunk"])

    embeddings = embedding_model.encode(texts)

    return embeddings    








