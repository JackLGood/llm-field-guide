from pathlib import Path
from openai import OpenAI

client = OpenAI(api_key="YOUR API KEY HERE")

def textToSpeech(response_text):
    """
    Converts text to OpenAI supported voice streamed to mp3 file.

    Parameter input: input text.
    Precondition: String.
    """
    with client.audio.speech.with_streaming_response.create(
        model="tts-1",
        voice="fable",
        input=response_text,
    ) as response:
        response.stream_to_file("response.mp3")
