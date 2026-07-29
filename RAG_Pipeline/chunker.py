from langchain_text_splitters import RecursiveCharacterTextSplitter
from RAG_Pipeline.config import CHUNK_SIZE ,CHUNK_OVERLAP

def split_text(document):

    """
    Split text into smaller chunks.
    """
    splitter = RecursiveCharacterTextSplitter(
        chunk_size = CHUNK_SIZE,
        chunk_overlap = CHUNK_OVERLAP
    )

    chunks = splitter.split_text(document['text'])

    chunk_documents = []

    for chunk in chunks:

        chunk_documents.append({
            "folder":document['folder'],
            "file_name":document['file_name'],
            "chunk":chunk
        })

    return chunk_documents    















