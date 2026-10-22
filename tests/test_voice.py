from device.microphone import record_audio
from device.speech_to_text import SpeechRecognizer


recognizer = SpeechRecognizer()

audio_file = record_audio()

text = recognizer.transcribe(audio_file)

print(f"You said: {text}")