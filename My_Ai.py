import pyttsx3
import datetime
import json
import random
import subprocess
import speech_recognition as sr 

engine = pyttsx3.init()
engine.say("Hello! I am hollali, your virtual assistant.")
engine.say("How may I assist you?")
engine.runAndWait()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wish_me():
    hour = datetime.datetime.now().hour
    if 6 <= hour < 12:
        speak("Good morning!")
    elif 12 <= hour < 18:
        speak("Good afternoon!")
    elif 18 <= hour < 24:
        speak("Good evening!")
    else:
        speak("Good night!")

    speak("How may I assist you today?")

def take_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio, language='en-in')
        print(f"User: {query}")
        return query
    except Exception as e:
        print(e)
        return None

def main():
    wish_me()

    while True:
        query = take_command()
        if query:
            query = query

            if 'time' in query:
                current_time = datetime.datetime.now().strftime("%I:%M %p")
                speak(f"The current time is {current_time}")

            elif 'date' in query:
                current_date = datetime.date.today().strftime("%A, %B %d, %Y")
                speak(f"Today is {current_date}")

            elif 'open notepad' in query:
                subprocess.Popen(["notepad.exe"])

            elif 'exit' in query or 'quit' in query:
                speak("Goodbye!")
                exit()

            else:
                speak("I'm not sure how to assist with that. Please ask something else.")

if __name__ == "__main__":
    main()
