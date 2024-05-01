# app.py
from flask import Flask, request, jsonify
from elasticsearch import Elasticsearch

app = Flask(__name__)
es = Elasticsearch()

@app.route("/ask", methods=["POST"])
def ask():
    data = request.get_json()  # Get the JSON payload from the request
    question = data["question"]  # Extract the question from the payload
    
    # Query Elasticsearch for relevant content
    response = es.search(
        index="pdf_data",
        body={
            "query": {
                "match": {
                    "content": question  # Search for matching content
                }
            }
        }
    )
    
    # Extract the most relevant result
    if response["hits"]["total"]["value"] > 0:
        answer = response["hits"]["hits"][0]["_source"]["content"]  # Get the content of the best match
    else:
        answer = "Sorry, I couldn't find an answer to your question."

    return jsonify({"answer": answer})

if __name__ == "__main__":
    app.run(debug=True, port=5000)  # Start the Flask server