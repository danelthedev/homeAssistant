import speech_recognition as sr

class SpeechToText:
    def __init__(self, keyword='Cornel'):
        self.r = sr.Recognizer()
        self.keyword = keyword
        print("Listening...")

        for index, name in enumerate(sr.Microphone.list_microphone_names()):
            print(f'{index}, {name}')

    def get_text(self):
        #wait for keyword to be said, then record
        with sr.Microphone(device_index=3) as source:
            audio = self.r.listen(source, 2, 10)
            try:
                text = self.r.recognize_google(audio, language='ro-RO')
                print("Debug: " + text)
                if text.startswith(self.keyword):
                    return text
            except:
                return "Keyword not said"

