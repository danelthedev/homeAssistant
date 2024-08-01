from ttsEngine import *
from chatGPTCom import *
from speechToText import *

class Asistent:
    numeAsistent = 'Cornel'

    tts = TTSEngine()
    gptCom = GPTCommunicator(numeAsistent)
    speechToText = SpeechToText(numeAsistent)

    status = True

    def __init__(self, numeAsistent='Cornel'):
        self.numeAsistent = numeAsistent

    def process_exit(self):
        self.tts.say("O zi buna!")
        self.status = False

    def process_gpt(self, mesajUser):
        res = self.gptCom.sendMessage(mesajUser)
        print(res)
        self.tts.say(res)

    def process_unknown(self, mesajUser):
        mesajUser = mesajUser.replace(self.numeAsistent, '')
        self.tts.say("Ai spus: " + mesajUser + ". Nu pot sa procesez acest mesaj.")

    def process_command(self, mesajUser):
        if 'exit' in mesajUser or 'quit' in mesajUser:
            self.process_exit()
        elif self.numeAsistent.lower() in mesajUser.lower():
            self.process_gpt(mesajUser)

    def run(self):
        while self.status:
            mesajUser = self.speechToText.get_text()

            if mesajUser is not None and mesajUser.startswith(self.numeAsistent):
                self.process_command(mesajUser.lower())
