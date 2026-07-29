import os
from docx import Document
import pandas as pd
from pypdf import PdfReader
from RAG_Pipeline.config import DATA_PATH


# Read TXT file and return its text.
def load_text(file_path):

    with open(file_path,"r",encoding="utf-8") as f:
       return f.read()


# Read CSV file and convert it to text.
def load_csv(file_path):

    df = pd.read_csv(file_path)   
    return df.to_string(index=False)


# Read DOCX file and return its text.
def load_docx(file_path):

    doc = Document(file_path)

    # Collect all paragraphs

    text = []
    for paragraph in doc.paragraphs:
      if paragraph.text.strip():
        text.append(
            paragraph.text.strip()
        )

    return "\n".join(text)    


# Read PDF file and return its text.
def load_pdf(file_path):

    reader = PdfReader(file_path)

    pages = []

    for page in reader.pages:

        page_text = page.extract_text()

        if page_text:
            pages.append(page_text)

    return "\n".join(pages)    


# Read all supported files inside Course_Materials.
def load_document():

    documents = []

    for course_folder,_ ,files in os.walk(DATA_PATH):

        for file in files:

            file_path = os.path.join(course_folder,file)

            if file_path.endswith(".txt"):
                text = load_text(file_path)

            elif file_path.endswith(".docx"):
                text = load_docx(file_path)

            elif file_path.lower().endswith(".pdf"):
                text = load_pdf(file_path) 

            elif file_path.endswith(".csv"):
                text = load_csv(file_path)       

            else:
                continue

            documents.append({
                "folder": os.path.basename(course_folder),
                "file_name":file,
                "text":text
            })

    return documents        
