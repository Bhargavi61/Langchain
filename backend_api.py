from fastapi import FastAPI
from pydantic import BaseModel
import faiss
import json
import numpy as np
from sentence_transformers import SentenceTransformer

app = FastAPI()

# Load FAISS index and metadata
index = faiss.read_index("faiss_index.index")
with open("metadata.json", "r") as metadata_file:
    metadata = json.load(metadata_file)

# Load the sentence transformer model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Define a request model
class QuestionRequest(BaseModel):
    question: str

@app.post("/query")
def query(data: QuestionRequest):
    question_embedding = model.encode([data.question])
    _, indices = index.search(question_embedding, 1)
    top_index = indices[0][0]
    return {"file_name": metadata["file_names"][top_index], "text": metadata["texts"][top_index]}
