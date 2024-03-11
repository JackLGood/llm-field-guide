from playsound import playsound
from pathlib import Path

def tts(client, text):
    speech_file = Path.cwd() / "chatgpt-test" / "speech.mp3"
    
    response = client.audio.speech.create(
        model = "tts-1",
        voice = "nova",
        input = text
    )
    response.stream_to_file(speech_file)
    playsound(speech_file.absolute().as_posix())
