import time

from gtts import gTTS
from pathlib import Path
from playsound3 import playsound

class TTSEngine:

    def __init__(self, language='ro'):
        self.language = language

    def say(self, text):
        speech_file_path = Path(__file__).parent / "speech.mp3"

        # Create the TTS audio file
        tts = gTTS(text=text, lang=self.language)
        tts.save(str(speech_file_path))

        # Play the TTS audio file
        playsound(str(speech_file_path))
        