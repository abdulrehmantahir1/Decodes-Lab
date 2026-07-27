import random

class Chatbot:
    def __init__(self):
        self.running = True
        
        # Define responses
        self.responses = {
            'greetings': {
                'keywords': ['hello', 'hi', 'hey', 'greetings', 'good morning', 'good afternoon', 'good evening'],
                'replies': [
                    "Hello! How can I help you today?",
                    "Hi there! Nice to meet you.",
                    "Hey! What brings you here?",
                    "Greetings! How are you doing?"
                ]
            },
            'farewells': {
                'keywords': ['bye', 'goodbye', 'exit', 'quit', 'see you', 'farewell', 'take care'],
                'replies': [
                    "Goodbye! Have a great day!",
                    "See you later! Take care.",
                    "Farewell! Nice talking to you.",
                    "Bye! Come back anytime."
                ]
            },
            'name': {
                'keywords': ['your name', 'who are you', 'what are you called'],
                'replies': [
                    "I'm ChatBot! What's your name?",
                    "My name is ChatBot. Nice to meet you!",
                    "I'm called ChatBot. And you are?"
                ]
            },
            'how_are_you': {
                'keywords': ['how are you', 'how do you do', 'how is it going'],
                'replies': [
                    "I'm doing great! Thanks for asking.",
                    "I'm functioning perfectly! How are you?",
                    "All good! What about you?"
                ]
            },
            'joke': {
                'keywords': ['tell me a joke', 'joke', 'funny', 'make me laugh'],
                'replies': [
                    "Why did the computer go to the doctor? It had a virus!",
                    "What do you call a bear with no teeth? A gummy bear!",
                    "Why don't scientists trust atoms? Because they make up everything!"
                ]
            },
            'help': {
                'keywords': ['help', 'what can you do', 'capabilities', 'features'],
                'replies': [
                    "I can chat with you, tell jokes, answer basic questions, and more!",
                    "I handle greetings, personal questions, jokes, and general conversation.",
                    "Ask me about my name, how I am, or tell me a joke!"
                ]
            },
            'default': {
                'keywords': [],
                'replies': [
                    "I'm not sure how to respond to that. Can you rephrase?",
                    "That's interesting! Tell me more.",
                    "I don't understand that yet. Try asking something else.",
                    "Could you please ask that differently?"
                ]
            }
        }
    
    def get_response(self, user_input):
        """Match user input to a response category using if-else logic"""
        user_input = user_input.lower().strip()
        
        # Check exit commands first
        if user_input in ['bye', 'goodbye', 'exit', 'quit']:
            self.running = False
            return random.choice([
                "Goodbye! Have a great day!",
                "See you later! Take care.",
                "Farewell! Nice talking to you."
            ])
        
        # Check empty input
        if not user_input:
            return "I didn't catch that. Could you say something?"
        
        # Check for keyword matches
        for category, data in self.responses.items():
            for keyword in data['keywords']:
                if keyword in user_input:
                    return random.choice(data['replies'])
        
        # Default response if no match
        return random.choice(self.responses['default']['replies'])
    
    def run(self):
        """Main loop - runs continuously until exit"""
        print("="*60)
        print("WELCOME TO CHATBOT")
        print("="*60)
        print("\nType 'help' to see what I can do.")
        print("Type 'bye' or 'exit' to end the chat.")
        print("-"*60)
        
        # Get user name
        user_name = input("\nChatbot: Hello! What's your name?\nYou: ").strip()
        if user_name.lower() in ['bye', 'exit', 'quit']:
            print("\nChatbot: Goodbye! Have a great day!")
            return
        
        print(f"\nChatbot: Nice to meet you, {user_name}!")
        
        # Main conversation loop
        while self.running:
            try:
                # Get user input
                user_input = input(f"\n{user_name}: ").strip()
                
                # Handle special commands
                if user_input.lower() == 'help':
                    print("\nChatbot: I can respond to:")
                    print("- Greetings (hello, hi, hey)")
                    print("- Questions about my name")
                    print("- Questions about how I am")
                    print("- Joke requests")
                    print("- Help requests")
                    print("- Farewells (bye, exit, quit)")
                    continue
                
                # Get and display response
                response = self.get_response(user_input)
                print(f"Chatbot: {response}")
                
            except KeyboardInterrupt:
                print("\n\nChatbot: Goodbye! Thanks for chatting!")
                break
            except Exception as e:
                print(f"Chatbot: Something went wrong. Please try again.")
        
        print("\n" + "="*60)
        print("THANK YOU FOR CHATTING!")
        print("="*60)


# Run the chatbot
if __name__ == "__main__":
    chatbot = Chatbot()
    chatbot.run()