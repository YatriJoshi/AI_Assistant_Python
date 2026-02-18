import random

name = input("Enter your name:")
print("Welcome", name, "to the Assistant Program!")

greetings=["hi", "hello", "hey","whats up","hii"]
mood_questions=["how are you?", "how r you", "how are you", "how r u"]
bye_statements=["bye", "goodbye", "see you","see ya","see you later","see you next time","never mind see you later"]
nice_statement=["nice i like it", "nice", "i like it", "cool", "awesome","great", "good job", "well done", "amazing", "fantastic", "wonderful", "excellent", "superb", "brilliant", "outstanding", "impressive", "marvelous", "terrific", "fabulous", "incredible", "magnificent"]
fallback_statement=["I am not sure I understood that.","Can you refrase that?","I am still learning. Try something else."]
while True:
    user = input("You: ").strip().lower()

    if user in greetings:
        print("Assistant: Hello!", name)

    elif user in mood_questions:
        print("Assistant: I'm learning every day!")
     
    elif user in nice_statement:
        print("Assistant: Thank you!")  
        
    elif user in bye_statements:
        print("Assistant: Goodbye! Have a great day!")  
        break

    else:
        print("Assistant:", random.choice(fallback_statement))

