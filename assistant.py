# Building AI Assistant in Python
import random
import datetime
USER_FILE = "users.txt"

def greet_user():
    try:
        with open(USER_FILE, "r") as file:
            name = file.read().strip()

        if name:
            print(f"Welcome back, {name}!")
            return name

    except FileNotFoundError:
        pass

    # If file doesn't exist or is empty
    name = input("Enter your name: ").strip()

    with open(USER_FILE, "w") as file:
        file.write(name)

    print(f"Nice to meet you, {name}!")
    return name

def handle_commands(user_input):
    if "time" in user_input:
        now = datetime.datetime.now()
        print("Assistant: The current time is", now.strftime("%H:%M:%S"))
        return True
    
    elif "date" in user_input:
        today = datetime.date.today()
        print("Assistant: Today's date is", today)
        return True
    
    elif user_input.startswith("add"):
        parts = user_input.split()
        
        if len(parts) == 3 and parts[1].isdigit() and parts[2].isdigit():
            result = int(parts[1] + int(parts[2]))
            print("Assistant: Result is", result)
        else:
            print("Assistant: Usage: add 5 10")
        return True
    
    elif user_input == "help":
        print("Assistant: Available commands:")
        print("- time -> Show current time")
        print("- date -> Show today's date")
        print("- add <num1> <num2> -> add numbers")
        print("-bye -> exit assistant")
        return True
    
    return False  
           
def run_assistant():
    greetings = ["hi", "hello", "hey", "whats up", "hii"]
    mood_questions = ["how are you", "how r you", "how r u"]
    bye_statements = ["bye", "goodbye", "see you", "see ya", "see you later", "see you soon", "see u soon", "see u later"]
    nice_statements = ["nice", "cool", "awesome", "great", "well done"]
    fallback_statements = [
        "I am not sure I understood that.",
        "Can you rephrase that?",
        "I am still learning. Try something else."
    ]
    thanks_statements = ["thank you", "thanks", "thx", "ty"]

    name = greet_user()

    while True:
        user = input("You: ").strip().lower()
        
        #1.Commands
        if handle_commands(user):
            continue
        
        #2. Conversation flow
        if user in greetings:
            print(f"Assistant: Hello, {name}!")

        elif user in mood_questions:
            print("Assistant: I'm learning every day!")

        elif user in nice_statements:
            print("Assistant: Thank you!")

        elif user in bye_statements:
            print("Assistant: Goodbye! Have a great day!")
            break
        elif user in thanks_statements:
            print("Assistant: You're welcome!")
        else:
            print("Assistant:", random.choice(fallback_statements))


run_assistant()