import subprocess

def install_requirements(requirements_file):
  """Installs packages from a requirements file."""
  subprocess.check_call(['pip', 'install', '-r', requirements_file])

# Example usage:
install_requirements('requirements.txt')
#pip install setuptools, SpeechRecognition, pyaudio, pyttsx3, text-to-speech
#Speech Recognition Part
import speech_recognition as sr
import pyttsx3
# Initialize the recognizer
recognizer = sr.Recognizer()
import chatbot
# Capture audio from the microphone
with sr.Microphone() as source:
    print("Please say something...")
    audio = recognizer.listen(source)

    try:
        # Use Google's speech recognition to convert audio to text
        text = recognizer.recognize_google(audio)
        print(f"You said: {text}")
    except sr.UnknownValueError:
        print("Sorry, I could not understand the audio.")
    except sr.RequestError:
        print("Could not request results from Google Speech Recognition service.")

engine=pyttsx3.init()
def speak(text):
    engine.say(text)
    engine.runAndWait()

import webbrowser
ltext=text.lower()
if"open google" in ltext:
    webbrowser.open("https://google.com/")
    response ="opening Google"
    print(response)
    speak(response)
    

elif"open youtube" in ltext:
    webbrowser.open("https://www.youtube.com/")
    print("Opening youtube")
    response ="opening Youtube"
    print(response)
    speak(response)

elif"play music" in ltext:
    webbrowser.open("https://www.youtube.com/results?search_query=music")
    response ="opening music on Youtube"
    print(response)
    speak(response)
else:
    print(chatbot.respond(ltext))
    speak(chatbot.respond(ltext))