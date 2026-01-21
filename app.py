from flask import Flask, request, jsonify
from flask_cors import CORS
from rag import get_answer

app = Flask(__name__)
CORS(app)

@app.route("/", methods=["GET"])
def health():
    return "AI backend is running successfully"

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json(force=True)
    question = data.get("question", "").strip()

    if not question:
        return jsonify({"answer": "Please ask a valid question."}), 400

    try:
        answer = get_answer(question)
        return jsonify({"answer": answer})
    except Exception:
        return jsonify({"answer": "Internal AI error. Please try again later."}), 500
