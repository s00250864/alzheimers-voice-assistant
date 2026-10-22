import os

from device.assistant import Assistant
from device.microphone import record_audio
from device.speech import speak
from device.speech_to_text import SpeechRecognizer


def main():

    assistant = Assistant()
    recognizer = SpeechRecognizer()

    print("Voice Assistant")
    print("Press ENTER to speak.")
    print("Type 'exit' to stop.\n")

    while True:

        user_input = input(
            "Press ENTER to speak: "
        )

        if user_input.lower().strip() == "exit":
            speak("Goodbye.")
            break

        audio_file = record_audio()

        try:
            command = recognizer.transcribe(audio_file)

            print(f"You said: {command}")

            if not command:
                response = "Sorry, I did not hear anything."

            else:
                response = assistant.process_command(command)

            print(f"Assistant: {response}")

            speak(response)

        except Exception as error:

            print(f"Speech recognition error: {error}")

            speak(
                "Sorry, I could not understand you."
            )

        finally:

            if os.path.exists(audio_file):
                os.remove(audio_file)


if __name__ == "__main__":
    main()