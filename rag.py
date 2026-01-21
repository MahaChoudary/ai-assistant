# rag.py
import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

# Configure the API
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

DATA_CONTEXT = ""

def load_data_once():
    global DATA_CONTEXT
    if DATA_CONTEXT:
        return

    texts = []
    if not os.path.exists("data"):
        return

    for file in os.listdir("data"):
        file_path = os.path.join("data", file)
        if os.path.isfile(file_path):
            with open(file_path, "r", encoding="utf-8") as f:
                texts.append(f.read())

    DATA_CONTEXT = "\n".join(texts)

def get_answer(question: str) -> str:
    load_data_once()

    prompt = f"""
You are a personal AI assistant for Maheen Hamid.
Answer ONLY from the information below.
Be clear and concise.

Information:
{DATA_CONTEXT}

Question:
{question}
"""

    # Use the correct API method
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content(prompt)

    return response.text
