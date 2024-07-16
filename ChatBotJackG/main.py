import os

from SpeechToText import speechToText
from RunAI import getResponse
from TextToSpeech import textToSpeech
from ProcessAndSendtoESP import process_audio_and_send

from openai import OpenAI

key = "YOUR API KEY HERE"
assistant_id = "asst_5u7H1dP27dK1TeIwzxzqJ98X"

def main():
    # Specify the MP3 file for speech-to-text conversion
    mp3_file = "query.mp3"

    # Convert the MP3 file to text
    user_input = speechToText(mp3_file)

    # Check if speech-to-text conversion was successful
    if user_input:
        # Process the text using the chatbot code
        response_text = getResponse(user_input)

        # Convert the chatbot's response text to speech
        filepath=textToSpeech(response_text)
        process_audio_and_send(filepath)
    else:
        print("No valid input received. Exiting.")

if __name__ == "__main__":
    main()
