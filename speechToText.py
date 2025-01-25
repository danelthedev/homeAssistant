import speech_recognition as sr


class RomanianSpeechToText:
    def __init__(self, keyword='Cornel'):
        self.keyword = keyword
        self.recognizer = sr.Recognizer()

    def listen_from_microphone(self, timeout=5, language='ro-RO'):
        """
        Capture audio from microphone and convert to text

        :param timeout: Maximum recording time in seconds
        :param language: Language code for Romanian
        :return: Recognized text or None if no speech detected
        """
        with sr.Microphone(device_index=2) as source:
            print("Listening...")

            try:
                # Adjust for ambient noise
                self.recognizer.adjust_for_ambient_noise(source, duration=1)

                # Listen to audio
                audio = self.recognizer.listen(source, timeout=timeout)

                # Recognize speech using Google Speech Recognition
                text = self.recognizer.recognize_google(audio, language=language)
                if text.startswith(self.keyword):
                    return text

            except sr.UnknownValueError:
                print("Nu s-a putut recunoaște speech")
                return None
            except sr.RequestError as e:
                print(f"Eroare la serviciul de recunoaștere: {e}")
                return None
