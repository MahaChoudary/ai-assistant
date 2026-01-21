from flask import Flask, request, jsonify
from flask_cors import CORS
from rag import get_answer
import os

app = Flask(__name__)
CORS(app)

@app.route("/", methods=["GET"])
def health():
    return "AI backend is running"

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    question = data.get("question", "")
    answer = get_answer(question)
    return jsonify({"answer": answer})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
