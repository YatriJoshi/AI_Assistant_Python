import random


def greet_user():
    name = input("Enter your name: ")
    print(f"Welcome {name} to the Assistant Program!")
    return name


def run_assistant():
    greetings = ["hi", "hello", "hey", "whats up"]
    mood_questions = ["how are you", "how r you", "how r u"]
    bye_statements = ["bye", "goodbye", "see you", "see ya"]
    nice_statements = ["nice", "cool", "awesome", "great", "well done"]
    fallback_statements = [
        "I am not sure I understood that.",
        "Can you rephrase that?",
        "I am still learning. Try something else."
    ]

    name = greet_user()

    while True:
        user = input("You: ").strip().lower()

        if user in greetings:
            print(f"Assistant: Hello, {name}!")

        elif user in mood_questions:
            print("Assistant: I'm learning every day!")

        elif user in nice_statements:
            print("Assistant: Thank you!")

        elif user in bye_statements:
            print("Assistant: Goodbye! Have a great day!")
            break

        else:
            print("Assistant:", random.choice(fallback_statements))


run_assistant()