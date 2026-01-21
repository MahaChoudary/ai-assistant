from flask import Flask, request, jsonify
from flask_cors import CORS
from rag import get_answer
import os

app = Flask(__name__)
CORS(app)

@app.route("/", methods=["GET"])
def health():
    return jsonify({"status": "ok", "message": "AI backend is running"})

@app.route("/chat", methods=["POST"])
def chat():
    try:
        data = request.get_json(force=True)
        question = data.get("question", "").strip()

        if not question:
            return jsonify({"answer": "Please ask a valid question."})

        answer = get_answer(question)
        return jsonify({"answer": answer})

    except Exception as e:
        print("CHAT ERROR:", e)
        return jsonify({
            "answer": "AI is busy or temporarily unavailable. Please try again."
        })

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
