from pdfminer.high_level import extract_text
from elasticsearch import Elasticsearch
import os

# Function to extract text from a PDF
def extract_text_from_pdf(pdf_path):
    return extract_text(pdf_path)

# Connect to Elasticsearch
es = Elasticsearch()

# Create the index if it doesn't exist
index_name = "pdf_data"
if not es.indices.exists(index_name):
    mapping = {
        "mappings": {
            "properties": {
                "filename": {"type": "text"},
                "content": {"type": "text"}
            }
        }
    }
    es.indices.create(index=index_name, body=mapping)

# Extract text from PDFs and index it
pdf_directory = "data/your_pdfs"  # Path to your PDFs
pdf_texts = []

# Extract text and index it in Elasticsearch
for filename in os.listdir(pdf_directory):
    if filename.endswith(".pdf"):
        file_path = os.path.join(pdf_directory, filename)
        text = extract_text_from_pdf(file_path)
        pdf_texts.append({
            "filename": filename,
            "content": text
        })
    
    if pdf_texts[-1]["content"].strip():  # Ensure it's not empty
        es.index(
            index=index_name,
            body={
                "filename": pdf_texts[-1]["filename"],
                "content": pdf_texts[-1]["content"]
            }
        )