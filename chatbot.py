print("🤖 Rule-Based Chatbot")
print("Type 'bye' to exit.\n")

while True:
    user_input = input("You: ").lower()

    if user_input in ["hi", "hello", "hey"]:
        print("Bot: Hello! How can I help you?")

    elif user_input == "how are you":
        print("Bot: I'm doing great! Thanks for asking.")

    elif user_input == "your name":
        print("Bot: I am a Rule-Based AI Chatbot.")
    
    elif user_input == "time":
        from datetime import datetime
        print("Bot:", datetime.now().strftime("%H:%M:%S"))

    elif user_input == "help":
        print("Bot: You can say hi, how are you, time, or bye.")

    elif user_input in ["bye", "exit", "quit"]:
        print("Bot: Goodbye! Have a nice day.")
        break

    else:
        print("Bot: Sorry, I don't understand that.")