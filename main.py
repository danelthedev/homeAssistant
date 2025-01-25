from chatGPTCom import GPTCommunicator
from speechToText import *
from tts import *
from assistantDisplay import AssistantDisplay


def main():
    numeAsistent = 'John'
    display = AssistantDisplay(numeAsistent)

    gptCom: GPTCommunicator = GPTCommunicator(numeAsistent)
    speechToText = SpeechToText(numeAsistent)

    def process_audio():
        try:
            mesajUser = speechToText.listen_from_microphone()

            if mesajUser is not None and mesajUser.startswith(numeAsistent):
                print(mesajUser.lower())

                res = gptCom.sendMessage(mesajUser)
                print(res)

                # Speak with animation
                display.speak_with_animation(res)

        except Exception as e:
            print(f"Error in audio processing: {e}")

        # Schedule next audio processing
        display.root.after(100, process_audio)

    # Start audio processing
    display.root.after(100, process_audio)

    # Run the display
    display.run()


if __name__ == "__main__":
    main()