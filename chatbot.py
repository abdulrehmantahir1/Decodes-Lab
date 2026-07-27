def get_response(message):
    # Dictionary for exact input matches
    responses = {
        "hello": "Hello! How can I help you?",
        "hi": "Hello! How can I help you?",
        "hey": "Hello! How can I help you?",
        "how are you": "I am doing great. Thanks for asking!",
        "what is your name": "My name is RuleBot.",
        "your name": "My name is RuleBot.",
        "who made you": "I was created as a rule-based AI chatbot project.",
        "thanks": "You're welcome!",
        "thank you": "You're welcome!",
        "help": """I can respond to:
- Greetings
- Name questions
- How are you
- Help
- Thanks
- Bye""",
        "bye": "Goodbye! Have a nice day.",
        "exit": "Goodbye! Have a nice day."
    }

    # Return matching response or default message
    return responses.get(message, "Sorry, I don't understand that.")

print("=" * 50)
print("         RULE-BASED AI CHATBOT")
print("=" * 50)
print("Type 'bye' or 'exit' to quit.\n")

while True:

    message = input("You: ").strip().lower()

    if not message:
        print("Bot: Please enter a message.")
        continue

    response = get_response(message)

    print(f"Bot: {response}")

    if message in ["bye", "exit"]:
        break