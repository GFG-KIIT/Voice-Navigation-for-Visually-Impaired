#speech recognition and text-to-speech system that listens for voice commands, perform actions like opening various websites, and responds using a chatbot. It will keep on asking until the user itself asks to exit.

import speech_recognition as sr
import pyttsx3
import webbrowser

# Initialize the recognizer and TTS engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

#Function to speak the text
def speak(text):
    engine.say(text)
    engine.runAndWait()

#capture audio from microphone
while True:
    with sr.Microphone() as source:
        print("Please say something...")
        audio = recognizer.listen(source)

        try:
            # Convert audio to text using Google's speech recognition
            text = recognizer.recognize_google(audio)
            print(f"You said: {text}")
        except sr.UnknownValueError:
            print("Sorry, I could not understand the audio.")
            speak("Sorry, I could not understand the audio.")
            continue           # Skip to the next iteration to keep asking for commands
        except sr.RequestError:
            print("Could not request results from Google Speech Recognition service.")
            speak("Could not request results from Google Speech Recognition service.")
            continue

    ltext = text.lower()

    if "exit" in ltext or "quit" in ltext:
        print("Exiting...")
        speak("Exiting...")
        break         # Exit the loop to terminate the program

    elif "open google" in ltext:
        webbrowser.open("https://google.com/")
        response = "Opening Google"
    elif "open youtube" in ltext:
        webbrowser.open("https://www.youtube.com/")
        response = "Opening YouTube"
    elif "play music" in ltext:
        webbrowser.open("https://www.youtube.com/results?search_query=music")
        response = "Playing music on YouTube"
    else:
        import chatbot         #check that chatbot module is available
        response = chatbot.respond(ltext)

    print(response)
    speak(response)