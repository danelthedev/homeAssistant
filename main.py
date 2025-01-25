import os
import sys


def speak_text(text):
    """
    Convert text to speech using pyttsx3 library

    Prerequisites:
    1. Install pyttsx3: 
       sudo apt-get update
       sudo apt-get install espeak
       pip3 install pyttsx3
    """
    try:
        import pyttsx3
    except ImportError:
        print("Error: pyttsx3 library not found. Please install it using 'pip3 install pyttsx3'")
        sys.exit(1)

    # Initialize the TTS engine
    engine = pyttsx3.init()

    # Optional: Adjust speech properties
    engine.setProperty('rate', 150)  # Speed of speech
    engine.setProperty('volume', 0.9)  # Volume (0.0 to 1.0)

    # Speak the text
    engine.say(text)
    engine.runAndWait()


def main():
    # Get text input from user
    text = input("Enter the text you want to speak: ")

    # Speak the text
    speak_text(text)


if __name__ == "__main__":
    main()