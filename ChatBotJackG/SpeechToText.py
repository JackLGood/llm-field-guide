from openai import OpenAI
client = OpenAI(api_key="YOUR API KEY HERE")

def speechToText(mp3_file):
    """
    Transcribes mp3 file to string. Supports multiple languages.

    Parameter input: mp3_file.
    Precondition: input is a mp3 file.
    """
    # open the audio file
    audio_file= open(mp3_file, "rb")
    # let openai do the dirty work, see transcriptions doc
    transcription = client.audio.transcriptions.create(
      model="whisper-1",
      file=audio_file
    )
    # return string of inputed speech
    return transcription.text
