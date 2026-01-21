import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise RuntimeError("GEMINI_API_KEY is missing")

genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")

def load_data():
    texts = []
    try:
        for file in os.listdir("data"):
            with open(f"data/{file}", "r", encoding="utf-8") as f:
                texts.append(f.read())
    except Exception as e:
        print("Data load error:", e)
    return texts

def get_answer(question: str) -> str:
    try:
        context = "\n".join(load_data())
        prompt = f"""
You are a personal AI assistant for Maheen Hamid.
Answer clearly and shortly using the information below.

Information:
{context}

Question:
{question}
"""
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        print("Gemini error:", e)
        return "AI is temporarily unavailable. Please try again."
