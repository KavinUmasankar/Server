# -*- coding: utf-8 -*-
"""
Created on Mon Jun  7 15:14:28 2021

@author: kavin
"""

import socket
import _thread
import sys

server = "192.168.1.96"
port = 5353

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))    
except socket.error as e:
    str(e)
    
s.listen()
print("Connecting...")

def threaded_client(conn):
    conn.send(str.encode("Connected!"))
    reply = ""
    while True:
        try:
            data = conn.recv(2048)
            reply = data.decode("utf-8")
            if not data:
                print("Disconnected")
                break
            else:
                print("Received: ", reply)
                print("Sending: ", reply)
            conn.sendall(str.encode(reply))
        except:
            break
    print("Lost Connection")
    conn.close()
    
while True:
    conn, addr = s.accept()
    print("Connected to: ", addr)
    
    _thread.start_new_thread(threaded_client, (conn,))