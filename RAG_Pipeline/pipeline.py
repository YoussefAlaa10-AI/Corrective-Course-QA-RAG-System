from RAG_Pipeline.loader import load_document
from RAG_Pipeline.cleaner import clean_text
from RAG_Pipeline.chunker import split_text
from RAG_Pipeline.embedding import create_embeddings
from RAG_Pipeline.vector_store import create_vector_database

def build_vector_database():

    """
    Read course files and build the vector database.
    """
    all_chunks = []

    documents = load_document()

    for document in documents:

        document = clean_text(document)

        chunks = split_text(document)

        all_chunks.extend(chunks)

    embeddings = create_embeddings(all_chunks)  

    create_vector_database(all_chunks,embeddings) 

def ask_question(question):

    """
    Answer a user question using Corrective RAG.
    """
    # Import after vector database exists
    from RAG_Pipeline.retriever import retrieve
    from RAG_Pipeline.evaluator import evaluate_context
    from RAG_Pipeline.LLM import generate_answer
    from RAG_Pipeline.rewrite_query import rewrite_query

    # First Retrieval
    retrieved_chunks = retrieve(question)

    rewritten_query = None

    # Evaluate retrieved context
    if evaluate_context(question, retrieved_chunks):
        answer = generate_answer(question,retrieved_chunks)

    else:
        # Rewrite query
        rewritten_query = rewrite_query(question)

        # Retrieve again
        retrieved_chunks = retrieve(rewritten_query)

        # Generate final answer
        answer = generate_answer(rewritten_query,retrieved_chunks)


    return answer, retrieved_chunks ,rewritten_query



    





     


           


