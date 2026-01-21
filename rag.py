import os
import google.generativeai as genai

print("GEMINI STABLE SDK ACTIVE")

# Railway reads env vars automatically
genai.configure(api_key=os.environ["GEMINI_API_KEY"])
model = genai.GenerativeModel("gemini-1.5-flash")

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")

def load_data():
    texts = []
    for file in os.listdir(DATA_DIR):
        file_path = os.path.join(DATA_DIR, file)
        with open(file_path, "r", encoding="utf-8") as f:
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
