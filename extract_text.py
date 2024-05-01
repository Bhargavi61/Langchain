# extract_text.py
from pdfminer.high_level import extract_text
import os

# Function to extract text from a PDF
def extract_text_from_pdf(pdf_path):
    return extract_text(pdf_path)

# Extract text from all PDFs in a directory
pdf_directory = "path/to/your/pdf/folder"
pdf_texts = []

for filename in os.listdir(pdf_directory):
    if filename.endswith(".pdf"):
        file_path = os.path.join(pdf_directory, filename)
        text = extract_text_from_pdf(file_path)
        pdf_texts.append({
            "filename": filename,
            "content": text
        })