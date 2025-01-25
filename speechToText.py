import sounddevice
import speech_recognition as sr


class SpeechToText:
    def __init__(self, keyword='John'):
        self.keyword = keyword
        self.recognizer = sr.Recognizer()

    def listen_from_microphone(self, timeout=60, language='en-US'):
        with sr.Microphone(device_index=2) as source:
            print("Listening...")

            try:
                # Adjust for ambient noise
                self.recognizer.adjust_for_ambient_noise(source, duration=1)

                # Listen to audio
                audio = self.recognizer.listen(source, timeout=timeout)

                # Recognize speech using Google Speech Recognition
                text: str = self.recognizer.recognize_google(audio, language=language)
                if self.keyword in text:
                    return text[text.rfind(self.keyword):]

            except sr.UnknownValueError:
                print("Nu s-a putut recunoaște speech")
                return None
            except sr.RequestError as e:
                print(f"Eroare la serviciul de recunoaștere: {e}")
                return None
