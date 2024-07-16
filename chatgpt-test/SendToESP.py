import ffmpegio
import numpy as np
import socket
import json
import time

nframes = 16  # read 16 frames at a time
mp3file = 'speech.mp3'
fullArray = []  # every value from the sound file
avgArray = []
smoothArray = []
mapArray = []

ESP_IP = "192.168.0.226"  # Replace with your ESP8266's IP address
ESP_PORT = 1234  # Same port number as in the Arduino code

def send_integer(num):
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.sendto(str(num).encode(), (ESP_IP, ESP_PORT))
        # response, _ = s.recvfrom(1024)
        # print(f"Received from ESP8266: {response.decode()}")

def process_audio_and_send(mp3file, nframes):
    with ffmpegio.open(mp3file, 'ra', blocksize=nframes, sample_fmt='dbl') as file:
        for i, indata in enumerate(file):
            volume_norm = np.linalg.norm(indata) * 10
            n0 = i * indata  # starting sample index
            fullArray.append(int(volume_norm))

    avgArray = avgValues(fullArray, 1000)
    smoothArray = smoothValues(avgArray, 10)
    mapArray = mapp(smoothArray, 0, 180)

    for i in range(len(mapArray)):
        # print(f'{i} out of {len(mapArray)}')
        send_integer(mapArray[i])
        time.sleep(0.2)

    # clear the queue
    for i in range(5):
        send_integer(0)
        time.sleep(0.1)

def avgValues(sampleArray, distance):
    newArray = []
    for val in range(0, len(sampleArray) - 1, distance):  # every 25th value in the original array
        summ = 0
        for val2 in range(0, distance):
            if (val + val2 < len(sampleArray)):
                summ = summ + sampleArray[val + val2]
        avg = summ / distance
        newArray.append(avg)
    return newArray

def smoothValues(sampleArray, steps):
    newArray = []
    for num in range(0, len(sampleArray) - 2):
        if sampleArray[num] > sampleArray[num + 1]:
            dif = (sampleArray[num] - sampleArray[num + 1]) / steps
            for num2 in range(0, steps):
                newArray.append(sampleArray[num] - (num2 * dif))
        else:
            dif = (sampleArray[num + 1] - sampleArray[num]) / steps
            for num2 in range(0, steps):
                newArray.append(sampleArray[num] + (num2 * dif))
    return newArray

def mapp(sampleArray, newLow, newHigh):
    newArray = []
    highest = sampleArray[0]
    lowest = sampleArray[0]
    for val in sampleArray:
        if val > highest:
            highest = val
        if val < lowest:
            lowest = val
    for val in sampleArray:
        newVal = round(newLow + ((val / (highest - lowest)) * newHigh))
        newArray.append(newVal)
    return newArray

# Call the function to process the audio and send data
#process_audio_and_send(mp3file, nframes)
