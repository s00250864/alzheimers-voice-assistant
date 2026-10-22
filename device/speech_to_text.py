from faster_whisper import WhisperModel


class SpeechRecognizer:

    def __init__(self):
        print("Loading speech recognition model...")

        self.model = WhisperModel(
            "tiny.en",
            device="cpu",
            compute_type="int8",
        )

        print("Speech recognition ready.")

    def transcribe(self, audio_file: str) -> str:
        """
        Convert an audio file into text.
        """

        segments, _ = self.model.transcribe(audio_file)

        text_parts = []

        for segment in segments:
            text_parts.append(segment.text)

        text = " ".join(text_parts)

        return text.strip()