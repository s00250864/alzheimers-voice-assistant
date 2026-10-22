import sounddevice as sd
from scipy.io.wavfile import write


SAMPLE_RATE = 16000


def record_audio(
    filename: str = "recording.wav",
    duration: int = 5,
) -> str:
    """
    Record audio from the default microphone.

    Returns the filename containing the recording.
    """

    print("Listening...")

    recording = sd.rec(
        int(duration * SAMPLE_RATE),
        samplerate=SAMPLE_RATE,
        channels=1,
        dtype="int16",
    )

    sd.wait()

    write(
        filename,
        SAMPLE_RATE,
        recording,
    )

    print("Recording complete.")

    return filename


if __name__ == "__main__":
    record_audio()