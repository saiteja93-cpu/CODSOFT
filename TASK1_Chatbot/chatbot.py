import datetime

print("=" * 50)
print("      Welcome to CodSoft AI Chatbot")
print("=" * 50)

name = input("Before we begin, what's your name? ")

print(f"\nHello {name}! Type 'bye' to exit.\n")

while True:
    user_input = input("You: ").lower().strip()

    if user_input in ["hello", "hi", "hey"]:
        print("Bot: Hello! How can I help you today?")

    elif "how are you" in user_input:
        print("Bot: I'm doing great! Thanks for asking.")

    elif "your name" in user_input:
        print("Bot: I am a Rule-Based AI Chatbot developed for CodSoft Internship.")

    elif "my name" in user_input:
        print(f"Bot: Your name is {name}.")

    elif "time" in user_input:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        print(f"Bot: Current time is {current_time}")

    elif "date" in user_input:
        current_date = datetime.datetime.now().strftime("%d-%m-%Y")
        print(f"Bot: Today's date is {current_date}")

    elif "help" in user_input:
        print("Bot: I can answer basic questions like greetings, date, time, and your name.")

    elif "thank" in user_input:
        print("Bot: You're welcome!")

    elif "internship" in user_input:
        print("Bot: The CodSoft Internship is a great opportunity to learn and grow in the field of software development.")

    elif user_input in ["bye", "exit", "quit"]:
        print("Bot: Goodbye! Have a wonderful day.")
        break

    else:
        print("Bot: Sorry, I don't understand that. Please try another question.") 
