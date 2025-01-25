from pygame import time
from chatGPTCom import GPTCommunicator
from speechToText import *
from tts import *
from assistantDisplay import AssistantDisplay
import threading

def main():
    numeAsistent = 'John'

    gptCom = GPTCommunicator(numeAsistent)
    speechToText = SpeechToText(numeAsistent)
    display = AssistantDisplay()

    try:
        while True:
            # Show silent state initially
            display.show_silent()

            mesajUser = speechToText.listen_from_microphone()

            if mesajUser is not None and mesajUser.startswith(numeAsistent):
                print(mesajUser.lower())

                res = gptCom.sendMessage(mesajUser)
                print(res)

                # Flag to control when to switch to silent mode
                is_talking = True

                # Play audio in a separate thread
                def play_audio():
                    speak_text(res)
                    nonlocal is_talking
                    is_talking = False

                audio_thread = threading.Thread(target=play_audio)
                audio_thread.start()

                # Display talking visuals while the assistant is "talking"
                while is_talking:
                    display.show_talking()
                    time.wait(500)  # Update visuals every 500ms

                # Ensure audio thread finishes
                audio_thread.join()

    except KeyboardInterrupt:
        print("Exiting...")
    finally:
        display.cleanup()


if __name__ == "__main__":
    main()
