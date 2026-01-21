import os
from dotenv import load_dotenv
from google import genai

print("GEMINI SDK ACTIVE")

load_dotenv()

# Create Gemini client (NEW SDK STYLE)
client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

# LOAD DATA ONCE (IMPORTANT)
DATA_CONTEXT = ""

def load_data_once():
    global DATA_CONTEXT
    texts = []
    for file in os.listdir("data"):
        file_path = os.path.join("data", file)
        if os.path.isfile(file_path):
            with open(file_path, "r", encoding="utf-8") as f:
                texts.append(f.read())
    DATA_CONTEXT = "\n".join(texts)

load_data_once()


def get_answer(question: str) -> str:
    prompt = f"""
You are a personal AI assistant for Maheen Hamid.
Answer ONLY from the information below.
Be clear and concise.

Information:
{DATA_CONTEXT}

Question:
{question}
"""

    response = client.models.generate_content(
        model="gemini-1.5-flash",
        contents=prompt
    )

    return response.text
