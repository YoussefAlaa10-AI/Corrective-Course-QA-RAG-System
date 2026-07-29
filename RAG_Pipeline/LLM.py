from RAG_Pipeline.config import LLM_MODEL
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser

model = ChatGoogleGenerativeAI(
    model=LLM_MODEL
)
parser = StrOutputParser()
chain = model | parser

def generate_answer(question,retrieved_chunks):

    chunks_list = []
    
    for chunk in retrieved_chunks:
        chunks_list.append(chunk['chunk'])

    context ="\n\n".join(chunks_list)  

    prompt = f"""
You are a helpful AI assistant.

Answer the user's question using ONLY the provided context.

If the answer is not found in the context, reply exactly:

I don't know.

Do not use your own knowledge.
Do not make up information.

Context:
{context}

Question:
{question}
""" 
    return chain.invoke(prompt)

