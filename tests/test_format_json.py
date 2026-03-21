"""
test_format_json.py — Prueba de Salida Estructurada JSON

Valida que el modelo local (ChatOllama / llama3.1) responda adecuadamente 
empleando el parámetro format="json" proporcionado por LangChain.
"""

from langchain_ollama import ChatOllama

def test():
    try:
        model = ChatOllama(model="llama3.1", format="json")
        res = model.invoke("Dime tu nombre y tu especialidad en un JSON.")
        print(f"Resultado: {res.content}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    test()
