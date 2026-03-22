"""
debug_gemini.py — Script de Depuración para Google Gemini

Prueba la conectividad y compatibilidad de nombres de modelo (`gemini-1.5-flash`, etc.)
utilizando el wrapper `langchain_google_genai` y la variable GOOGLE_API_KEY.
"""

import os
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")
print(f"Key present: {bool(api_key)}")

models_to_try = ["gemini-1.5-flash", "gemini-1.5-pro", "gemini-pro"]

for model in models_to_try:
    print(f"\nTesting model: {model}")
    try:
        llm = ChatGoogleGenerativeAI(model=model, google_api_key=api_key)
        res = llm.invoke("Hi")
        print(f"SUCCESS with {model}: {res.content}")
        break
    except Exception as e:
        print(f"FAILED with {model}: {e}")
