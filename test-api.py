import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
print(f"API Key loaded: {api_key[:10]}..." if api_key else "ERROR: No API key found!")

try:
    # Configure the API
    genai.configure(api_key=api_key)
    
    print("\n✓ API configured successfully")
    
    # List available models
    print("\n📋 Listing all available models...\n")
    for m in genai.list_models():
        if 'generateContent' in m.supported_generation_methods:
            print(f"  ✓ {m.name}")
    
    print("\n🧪 Testing gemini-1.5-flash...\n")
    
    # Test with gemini-1.5-flash
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content("Say 'Hello, I am working!' in one sentence.")
    
    print("✅ SUCCESS!")
    print(f"Response: {response.text}")
    
except Exception as e:
    print(f"\n❌ ERROR: {type(e).__name__}")
    print(f"Message: {str(e)}")
    print("\nThis means there's an issue with your API key or account setup.")
    print("Go to: https://aistudio.google.com/apikey")
    print("1. Delete your current API key")
    print("2. Create a NEW API key")
    print("3. Update your .env file")