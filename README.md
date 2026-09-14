# 🤖 Corrective Course Q&A RAG System

An end-to-end **Corrective Retrieval-Augmented Generation (Corrective RAG)** system for answering questions from course materials.

The system evaluates retrieved context before generating an answer. If the context is weak or irrelevant, it automatically rewrites the query and retrieves relevant information again.

## ✨ Features

- 📄 Supports PDF, DOCX, TXT, and CSV files
- 🧹 Text cleaning and preprocessing
- ✂️ Document chunking
- 🔢 Sentence Transformer embeddings
- 🗄️ FAISS vector database
- 🔍 Semantic retrieval
- 🧠 Context evaluation
- 🔄 Automatic query rewriting
- 💬 Answer generation using Google Gemini
- 📚 Source document references
- 🖥️ Interactive Gradio interface

## 🔄 Pipeline

```text
Documents
   ↓
Loader
   ↓
Cleaner
   ↓
Chunker
   ↓
Embeddings
   ↓
FAISS
   ↓
Retriever
   ↓
Context Evaluator
   ↓
 ┌───────────────┐
 │ Context Good? │
 └───────┬───────┘
     Yes │   No
         │    ↓
         │  Query Rewriting
         │    ↓
         │  Retrieve Again
         ↓    ↓
       LLM → Answer
              ↓
           Sources

```

## 🛠️ Technologies
Python
LangChain
Google Gemini
Sentence Transformers
FAISS
Gradio
Pandas
PyPDF
python-docx

## 📁 Project Structure
```text
Corrective Course Q&A RAG System/
│
├── RAG_Pipeline/
│   ├── loader.py
│   ├── cleaner.py
│   ├── chunker.py
│   ├── embedding.py
│   ├── vector_store.py
│   ├── retriever.py
│   ├── evaluator.py
│   ├── rewrite_query.py
│   ├── LLM.py
│   └── pipeline.py
│
├── data/
├── app.py
├── config.py
└── README.md
```
