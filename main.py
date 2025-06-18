import nltk
from nltk.chat.util import Chat, reflections

pairs = [
    ["hi|hello", ["Hi there! How can I assist you?"]],
    ["name|who are you", ["I'm a simple chatbot built with NLTK!"]],
    ["help|what can you do", ["I can reply to greetings, names, or help. Try 'hi' or 'bye'."]],
    ["bye|goodbye|exit", ["See you later!"]],
    ["(.*)", ["I didn't get that. Try 'hi', 'help', or 'bye'."]]
]

chatbot = Chat(pairs, reflections)

def run_chatbot():
    print("Type 'exit' to stop")
    while True:
        user_input = input("You: ")
        response = chatbot.respond(user_input)
        print("Bot:", response)
        if user_input.lower() in ["exit", "bye", "goodbye"]:
            break

nltk.download("punkt")
run_chatbot()