"""
debug_gemini_new_sdk.py — Debug con SDK Nativo de Google GenAI

Prueba de conexión con el nuevo cliente `google-genai` para enviar instrucciones
al modelo de forma directa sin dependencias de terceros (como LangChain).
"""

import os
from google import genai
from dotenv import load_dotenv

load_dotenv()

# Map GOOGLE_API_KEY to GEMINI_API_KEY if needed, or pass explicitly
api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    # Try GEMINI_API_KEY
    api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    print("Error: GOOGLE_API_KEY or GEMINI_API_KEY not found in environment.")
    exit(1)

print(f"Using API Key: {api_key[:5]}...")

try:
    client = genai.Client(api_key=api_key)
    
    # Trying the user's requested model
    user_model = "gemini-3-flash-preview"

    print(f"Attempting to generate with {user_model}...")
    response = client.models.generate_content(
        model=user_model, 
        contents="Explain how AI works in a few words"
    )
    print("Response received:")
    print(response.text)

except Exception as e:
    print(f"Error occurred: {e}")
