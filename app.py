from flask import Flask, request, jsonify
from flask_cors import CORS
from rag import get_answer
import os
import traceback

app = Flask(__name__)
CORS(app)

# Health check (VERY IMPORTANT for Railway)
@app.route("/", methods=["GET"])
def health():
    return jsonify({"status": "ok"}), 200


@app.route("/chat", methods=["POST"])
def chat():
    try:
        data = request.get_json(force=True)
        question = data.get("question", "").strip()

        if not question:
            return jsonify({"answer": "Please ask a valid question."}), 400

        answer = get_answer(question)
        return jsonify({"answer": answer}), 200

    except Exception as e:
        # LOG ERROR SO RAILWAY CAN SEE IT
        print("ERROR IN /chat")
        traceback.print_exc()

        return jsonify({
            "error": "Internal server error",
            "details": str(e)
        }), 500


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
