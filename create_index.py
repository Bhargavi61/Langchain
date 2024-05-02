from sentence_transformers import SentenceTransformer
import faiss
import json
import numpy as np

# Load your extracted data
with open("extracted_data.json", "r") as json_file:
    extracted_data = json.load(json_file)

# Use a sentence transformer to create embeddings
model = SentenceTransformer('all-MiniLM-L6-v2')

texts = [item["text"] for item in extracted_data]
embeddings = model.encode(texts)

# Create a FAISS index
index = faiss.IndexFlatL2(embeddings.shape[1])
index.add(embeddings)

# Save the index to disk
faiss.write_index(index, "faiss_index.index")

# Save additional metadata (file names, etc.)
metadata = {"texts": texts, "file_names": [item["file_name"] for item in extracted_data]}
with open("metadata.json", "w") as metadata_file:
    json.dump(metadata, metadata_file)
