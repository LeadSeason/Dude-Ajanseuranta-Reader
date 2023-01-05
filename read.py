#!/home/tonnikala/Programming/rfid-pytest/venv/bin/python3

import requests
import json
from time import sleep as s
import RPi.GPIO as GPIO
from mfrc522 import MFRC522
import sys

KEY = [0xFF,0xFF,0xFF,0xFF,0xFF,0xFF]
BLOCK_ADDRS = [8, 9, 10]


SERVER_ADDRESS = 'http://192.168.192.11:8080/test'

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

def main():
    READER = MFRC522()
    id = read_no_block(READER)
    while 1:
        while not id:
            id = read_no_block(READER)

        print(f"{id}")

        try:
            # Post id to server to be processed
            r = requests.post(SERVER_ADDRESS, json={"uid": id})
            if r.status_code == 200:
                pass
            else:
                print("failed to upload")
                print(r.status_code)

        # Using exception if upload failed so doesnt crash the program
        except Exception as e:
            print("failed to upload")
            print(e)

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
                        
