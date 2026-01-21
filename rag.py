import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = None
cached_context = None


def load_data():
    texts = []
    base_path = os.path.join(os.path.dirname(__file__), "data")

    for file in os.listdir(base_path):
        with open(os.path.join(base_path, file), "r", encoding="utf-8") as f:
            texts.append(f.read())

    return "\n".join(texts)


def get_answer(question):
    global model, cached_context

    if model is None:
        model = genai.GenerativeModel("gemini-1.5-flash")

    if cached_context is None:
        cached_context = load_data()

    prompt = f"""
You are a personal AI assistant for Maheen Hamid.
Answer briefly and clearly using the information below only.

Information:
{cached_context}

Question:
{question}
"""

    response = model.generate_content(prompt)
    return response.text
