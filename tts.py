import os
from gtts import gTTS
import pygame

def speak_text(text, language='en'):
    """
    Convert text to speech using Google Text-to-Speech

    Prerequisites:
    pip3 install gtts pygame
    """
    # Create audio file
    tts = gTTS(text=text, lang=language)
    tts.save("/tmp/speech.mp3")

    # make the file faster
    os.system("ffmpeg -hide_banner -loglevel error -i  /tmp/speech.mp3 -filter:a 'atempo=1.2' /tmp/speech2.mp3")

    # Initialize pygame mixer
    pygame.mixer.init()
    pygame.mixer.music.load("/tmp/speech2.mp3")
    pygame.mixer.music.play()

    # Wait for playback to finish
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

    # Clean up temporary file
    os.remove("/tmp/speech.mp3")
    os.remove("/tmp/speech2.mp3")
