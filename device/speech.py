import pyttsx3

def speak(text: str) -> None:
    """
    Speak the supplied text using text-to-speech.
    """

    engine = pyttsx3.init()

    engine.say(text)
    engine.runAndWait()