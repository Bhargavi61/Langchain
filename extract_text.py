import PyPDF2
import os

# Define a function to extract text from PDFs
def extract_text_from_pdfs(pdf_folder):
    extracted_data = []
    for file in os.listdir(pdf_folder):
        if file.endswith(".pdf"):
            file_path = os.path.join(pdf_folder, file)
            with open(file_path, 'rb') as f:
                pdf_reader = PyPDF2.PdfFileReader(f)
                pdf_text = ''
                for page_num in range(pdf_reader.getNumPages()):
                    pdf_text += pdf_reader.getPage(page_num).extractText()
                extracted_data.append({"file_name": file, "text": pdf_text})
    return extracted_data

# Save extracted data to a JSON file
import json
pdf_folder = "path/to/your/pdfs"
extracted_data = extract_text_from_pdfs(pdf_folder)
with open("extracted_data.json", "w") as json_file:
    json.dump(extracted_data, json_file)
