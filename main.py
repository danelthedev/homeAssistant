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

                # Use a separate thread to manage audio and visuals
                def play_audio_with_visuals():
                    # Alternate talking images while audio plays
                    while True:
                        display.show_talking()
                        time.wait(1000)
                        if not pygame.mixer.music.get_busy():
                            break

                # Start the visual thread and play audio
                visual_thread = threading.Thread(target=play_audio_with_visuals)
                visual_thread.start()
                speak_text(res)

                # Wait for the visual thread to finish
                visual_thread.join()

    except KeyboardInterrupt:
        print("Exiting...")
    finally:
        display.cleanup()


if __name__ == "__main__":
    main()
