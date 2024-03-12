from dotenv import load_dotenv
load_dotenv()

import json

from openai import OpenAI
from pathlib import Path

from SpeechToText import stt
from TextToSpeech import tts
from MarkerDetection import Detector

client = OpenAI()
detector = Detector()

json_file = open(Path.cwd() / "chatgpt-test" /"exhibits" / "met.json")
json_data = json.load(json_file)

if __name__ == "__main__":
    museum_name = json_data['museum']
    print(f'Welcome to the {museum_name} Museum')

    exhibits = json_data['exhibits']
    ex_id = input('Enter to start tracking (N to exit): ')

    while not ex_id.upper() == 'N':
      marker = detector.find_first_marker()

      ex = exhibits[str(marker)]

      print(f'You are at the "{ex["title"]}" exhibit. Ask me a question!')
      question = stt(client)
      print(question)

      # Create chat completion
      completion = client.chat.completions.create(
         model="gpt-3.5-turbo",
         messages=[
            {
               "role": "system",
               "content": ex['system']
            },
            {
               "role": "user",
               "content": question
            }
         ]
      )
      response = completion.choices[0].message.content
      print(response)

      tts(client, response)

      ex_id = input('Enter the ID of the exhibit (N to exit): ')
    
