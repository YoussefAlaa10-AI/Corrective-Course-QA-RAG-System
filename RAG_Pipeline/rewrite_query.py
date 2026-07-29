from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from RAG_Pipeline.config import LLM_MODEL

model = ChatGoogleGenerativeAI(
    model=LLM_MODEL
)
parser = StrOutputParser()
chain = model | parser

def rewrite_query(question):
    prompt = f"""
You are a query rewriting assistant.

Rewrite the following question to improve document retrieval.

Keep the same meaning.
Do not answer the question.
Return only the rewritten question.

Question:
{question}
"""
    return chain.invoke(prompt)