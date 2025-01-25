import os
from gtts import gTTS
import pygame


def speak_text(text, language='ro'):
    """
    Convert text to speech using Google Text-to-Speech

    Prerequisites:
    pip3 install gtts pygame
    """
    # Create audio file
    tts = gTTS(text=text, lang=language)
    tts.save("/tmp/speech.mp3")

    # Initialize pygame mixer
    pygame.mixer.init()
    pygame.mixer.music.load("/tmp/speech.mp3")
    pygame.mixer.music.play()

    # Wait for playback to finish
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

    # Clean up temporary file
    os.remove("/tmp/speech.mp3")


def main():
    text = input("Enter the text you want to speak: ")
    speak_text(text)


if __name__ == "__main__":
    main()