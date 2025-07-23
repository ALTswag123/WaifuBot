import requests

def chat_with_ollama():
    print("Local Chatbot). Type 'exit' to quit.\n")
    history = [
        {"role": "system", "content": "You are a cute, kawaii, uwu e-girl chatbot that can act out and play along with made up scenarios upon the users request. you speak english"}
    ]

    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break

        history.append({"role": "user", "content": user_input})

        response = requests.post(
            "http://localhost:11434/api/chat",
            json={
                "model": "mistral",  # or "llama3"
                "messages": history,
                "stream": False
            }
        )

        data = response.json()
        reply = data['message']['content']
        print(f"Bot: {reply}\n")

        history.append({"role": "assistant", "content": reply})

if __name__ == "__main__":
    chat_with_ollama()
