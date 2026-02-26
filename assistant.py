import random
import datetime
import speech_recognition as sr
import pyttsx3

engine = pyttsx3.init()
engine.setProperty("rate", 165)  # slower = clearer
print("=== ASSISTANT STARTED ===")

def speak_name(name):
    # Force correct pronunciation
    phonetic = "yaa tree"   # <- THIS is the key
    engine.say(phonetic)
    engine.runAndWait()
    
def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio)
        print("You:", command)
        return command.lower()
    except sr.UnknownValueError:
        speak("Sorry, I did not understand.")
        return ""
    except sr.RequestError:
        speak("Speech service is unavailable.")
        return ""

USER_FILE = "users.txt"

def greet_user():
    try:
        with open(USER_FILE, "r") as file:
            name = file.read().strip()
        if name:
           print(f"Assistant: Welcome back, {name}")
        engine.say("Welcome back")
        speak_name(name)
        return name
    except FileNotFoundError:
        pass

    name = input("Enter your name: ").strip()
    with open(USER_FILE, "w") as file:
        file.write(name)

    speak(f"Nice to meet you, {name}")
    return name

def handle_commands(user_input):
    if "time" in user_input:
        now = datetime.datetime.now()
        speak(f"The current time is {now.strftime('%H:%M:%S')}")
        return True

    if "date" in user_input:
        today = datetime.date.today()
        speak(f"Today's date is {today}")
        return True

    if user_input.startswith("add"):
        parts = user_input.split()
        if len(parts) != 3:
            speak("Usage is add 5 10")
            return True

        try:
            result = float(parts[1]) + float(parts[2])
            speak(f"Result is {result}")
        except ValueError:
            speak("Please say numbers")
        return True

    if "help" in user_input:
        speak("You can ask time, date, add numbers, or say bye")
        return True

    return False

def run_assistant():
    name = greet_user()
    speak("Assistant is ready")

    while True:
        text = listen()
        if not text:
            continue

        if "bye" in text or "exit" in text:
            speak("Goodbye")
            break

        if not handle_commands(text):
            speak("I did not understand")

# 🔴 THIS LINE IS CRITICAL
run_assistant()