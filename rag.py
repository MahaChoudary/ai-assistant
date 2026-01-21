import os
from dotenv import load_dotenv
import google.generativeai as genai

print("GEMINI STABLE SDK ACTIVE")

load_dotenv()

# ✅ safe API key load
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("GEMINI_API_KEY not found in environment variables")

genai.configure(api_key=api_key)

model = genai.GenerativeModel("models/gemini-1.5-flash")


def load_data():
    texts = []

    # ✅ IMPORTANT SAFETY CHECK
    if not os.path.exists("data"):
        print("⚠️ data folder not found, running without RAG data")
        return texts

    for file in os.listdir("data"):
        file_path = os.path.join("data", file)
        if os.path.isfile(file_path):
            with open(file_path, "r", encoding="utf-8") as f:
                texts.append(f.read())

    return texts


def get_answer(question):
    context_list = load_data()
    context = "\n".join(context_list) if context_list else "No additional context available."

    prompt = f"""
You are a personal AI assistant for Maheen Hamid.
Answer clearly and naturally.

Context:
{context}

Question:
{question}
"""

    response = model.generate_content(prompt)
    return response.text
