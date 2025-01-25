from chatGPTCom import GPTCommunicator
from speechToText import *
from tts import *

def main():
    numeAsistent = 'John'
    gptCom: GPTCommunicator = GPTCommunicator('John')

    speechToText = RomanianSpeechToText(numeAsistent)
    while True:
        mesajUser = speechToText.listen_from_microphone()

        if mesajUser is not None and mesajUser.startswith(numeAsistent):
            print(mesajUser.lower())
            res = gptCom.sendMessage(mesajUser)
            print(res)
            speak_text(res)



if __name__ == "__main__":
    main()