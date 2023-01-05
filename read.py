#!/home/tonnikala/Programming/rfid-pytest/venv/bin/python3

import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522()

old = 0

while 1:
    id, name = reader.read()
    print(f"{id}:{name}")

GPIO.cleanup()
