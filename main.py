#!/home/tonnikala/Programming/rfid-pytest/venv/bin/python3

import requests
import json
import time
import RPi.GPIO as GPIO
from mfrc522 import MFRC522
import sys

KEY = [0xFF,0xFF,0xFF,0xFF,0xFF,0xFF]
BLOCK_ADDRS = [8, 9, 10]

SERVER_ADDRESS = 'https://dudeworktimemanagment.leadseason.eu'
SERVER_POST_PATH = "/api/v1/card/read"

def read_no_block(READER):
    (status, TagType) = READER.MFRC522_Request(READER.PICC_REQIDL)
    if status != READER.MI_OK:
        return None
    (status, uid) = READER.MFRC522_Anticoll()
    if status != READER.MI_OK:
        return None
    id = uid_to_num(uid)
    return id


def uid_to_num(uid):
    n = 0
    for i in range(0, 5):
        n = n * 256 + uid[i]
    return n

def beepGood():
    buzzerPin = 21

    GPIO.setup(buzzerPin, GPIO.OUT)

    buzzer = GPIO.PWM(buzzerPin, 443)
    buzzer.start(10)

    buzzer.ChangeFrequency(600)
    time.sleep(0.1)
    buzzer.stop()
    time.sleep(0.05)
    buzzer.start(10)
    buzzer.ChangeFrequency(1000)
    time.sleep(0.1)
    buzzer.stop()


def beepBad():
    buzzerPin = 21

    GPIO.setup(buzzerPin, GPIO.OUT)

    buzzer = GPIO.PWM(buzzerPin, 443)
    buzzer.start(10)

    buzzer.ChangeFrequency(600)
    time.sleep(0.1)
    buzzer.stop()
    time.sleep(0.05)
    buzzer.start(10)
    buzzer.ChangeFrequency(400)
    time.sleep(0.1)
    buzzer.stop()


def main():
    GPIO.setmode(GPIO.BCM)
    READER = MFRC522()
    id = read_no_block(READER)
    while 1:
        while not id:
            id = read_no_block(READER)
            time.sleep(0.4)

        print(f"Card id: {id}", file=sys.stderr)

        try:
            # Post id to server to be processed
            r = requests.post(SERVER_ADDRESS+SERVER_POST_PATH, json={"uid": id})
            print({"uid": id})
            if r.status_code == 200:
                beepGood()
            else: 
                print("failed to upload:", r.status_code, file=sys.stderr)
                beepBad()

        # Using exception if upload failed so doesnt crash the program
        except Exception as e:
            print("failed to upload:", e, file=sys.stderr)
            beepBad()

        # Wait untill card leaves range
        # hacky solution because reader returns None every other call
        cardInRange = id   # Used to Check if same card
        index = 0          # Index used to check how many times was false
        while True:
            id = read_no_block(READER)
            if id == cardInRange:
                # if the same card detected reset index count to 0
                index = 0
            if index > 10:
                # if not present for 10 loops exit
                break
            index += 1
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass

    finally:
        GPIO.cleanup()
                        
