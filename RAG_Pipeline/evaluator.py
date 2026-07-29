from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from RAG_Pipeline.config import LLM_MODEL

model = ChatGoogleGenerativeAI(
    model=LLM_MODEL
)
parser = StrOutputParser()
chain = model | parser

def evaluate_context(question, retrieved_chunks):

    chunks_list = []
        
    for chunk in retrieved_chunks:
        chunks_list.append(chunk['chunk'])
    
    context ="\n\n".join(chunks_list)

    prompt = f"""
You are an evaluator.

Determine whether the retrieved context is sufficient to answer the user's question.

Reply with ONLY one word:

YES
or
NO

Question:
{question}

Context:
{context}
""" 
    response = chain.invoke(prompt).strip().upper()

    return response=="YES"
   