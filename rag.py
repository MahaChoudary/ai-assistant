import os
from dotenv import load_dotenv
import google.generativeai as genai

print("GEMINI STABLE SDK ACTIVE")

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel('gemini-2.5-flash')

def load_data():
    texts = []
    for file in os.listdir("data"):
        with open(f"data/{file}", "r", encoding="utf-8") as f:
            texts.append(f.read())
    return texts

def get_answer(question):
    context = "\n".join(load_data())
    prompt = f"""
You are a personal AI assistant for Maheen Hamid.
Answer the question ONLY using the information below.
Be clear, short, and natural.

Information:
{context}

Question:
{question}
"""
    response = model.generate_content(prompt)
    return response.text