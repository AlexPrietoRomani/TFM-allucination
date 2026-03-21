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
