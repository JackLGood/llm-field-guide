import sounddevice as sd
from scipy.io.wavfile import write
from pathlib import Path

fs = 44100
rec_file = Path.cwd() / "chatgpt-test" / "rec.mp3"

def stt(client, dur=5):
    rec = sd.rec(int(dur * fs), samplerate=fs, channels=1)
    sd.wait()
    write(rec_file, fs, rec)

    audio = open(rec_file, 'rb')
    transcription = client.audio.transcriptions.create(
        model ="whisper-1",
        file = audio
    )

    return transcription.text
