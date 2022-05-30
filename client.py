from pydoc import cli
import socket
import pickle
import threading
import datetime
import time
from time import sleep
from Tasks import *
 
HEADER = 64
PORT = 5050
DISCONNECT_MESSAGE = "!DISCONNECT"
CLIENT = socket.gethostbyname(socket.gethostname())
SERVER =  "192.168.43.135"
ADDR = (SERVER, PORT)
PERIOD = 10
KEY = 10

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def start():
    print("-------[[CLIENTE]]-------")
    print(f"[LISTENING] Client is listening on {CLIENT}")
    thread = threading.Thread(target=listen)
    thread.start()
    
def listen():
    print(f"THREAD listening on {CLIENT}")
    while handle_updates():
        print(datetime.datetime.now())
        sleep(PERIOD)
    client.close()
    print("Se ha cerrado la conexion")

def handle_updates():
    connected = True 
    print("EJECUTANDO HANDLE UPDATES")
    print("CONEXION ",connected)
    print("ENVIADO UPDATE")
    sendMsg("UPDATE")
    
    msg_length = pickle.loads(client.recv(HEADER))
    if msg_length:
        msg_length = int(msg_length)
        msg = pickle.loads(client.recv(msg_length))
        for i in msg:
            msg[i] = decrypt(msg[i])
        print(f"[NEW MESSAGE] from {ADDR}")
        print(msg)
        if msg == DISCONNECT_MESSAGE:
            connected=False
        elif msg == "------Actualizacion":
            print("He recibido la actualización del UPDATE")
        else:
            print(msg)    

    return connected

    

def sendMsg(msg):
    print("ENVIO TASK  >>>>",msg)
    for i in msg:
        msg[i] = encrypt(msg[i])
    message = pickle.dumps(msg)
    msg_length = len(message)
    send_length = pickle.dumps(str(msg_length))
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)

def encrypt(text):
    result = ""
    for i in range(len(text)):
        char = text[i]
      
        if (char.isupper()):
            result += chr((ord(char) + KEY - 65) % 26 + 65)
        else:
            result += chr((ord(char) + KEY - 97) % 26 + 97)
    return result

def decrypt(text):
    result = ""
    for i in range(len(text)):
        char = text[i]
      
        if (char.isupper()):
            result += chr((ord(char) - KEY - 65) % 26 + 65)
        else:
            result += chr((ord(char) - KEY - 97) % 26 + 97)
    return result

start()
