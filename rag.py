import os
from dotenv import load_dotenv
import google.genai as genai

print("GEMINI SDK ACTIVE")

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-1.5-flash")

# LOAD DATA ONCE (IMPORTANT)
DATA_CONTEXT = ""

def load_data_once():
    global DATA_CONTEXT
    texts = []
    for file in os.listdir("data"):
        with open(os.path.join("data", file), "r", encoding="utf-8") as f:
            texts.append(f.read())
    DATA_CONTEXT = "\n".join(texts)

load_data_once()


def get_answer(question):
    prompt = f"""
You are a personal AI assistant for Maheen Hamid.
Answer ONLY from the information below.
Be clear and concise.

Information:
{DATA_CONTEXT}

Question:
{question}
"""
    response = model.generate_content(prompt)
    return response.text
