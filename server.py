from io import SEEK_SET
import socket 
import threading
import pickle
from Tasks import *
from time import sleep
import datetime
from editTxt import *
import threading



HEADER = 64
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
PERIOD = 0.5
KEY = 10

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

tasks = Tasks()

def queueTask(task):
    tasks.addTask(task)

def createTask(id, args):
    print(args)
    queueTask(Task(args))

def sendMsg(conn, msg):
    for elem in msg:
       elem = encrypt (elem)
    message = pickle.dumps(msg)
    msg_length = len(message)
    send_length = pickle.dumps(str(msg_length))
    send_length += b' ' * (HEADER - len(send_length))
    conn.send(send_length)
    conn.send(message)

def listen(conn,addr,id):
    
    while handle_client(conn,addr,id): pass
    sleep(PERIOD)
    conn.close()


def handle_client(conn, addr, id):
    connected = True
    msg_length = pickle.loads(conn.recv(HEADER))
    if msg_length:
        msg_length = int(msg_length)
        msg = pickle.loads(conn.recv(msg_length))
        for i in msg:
            msg[i] = decrypt(msg[i])
        print(msg)
        if msg == DISCONNECT_MESSAGE:
            connected=False
        elif msg == "UPDATE":
            sendMsg(conn,"------Actualizacion")
        else:
            createTask(id,msg)

    return connected



def executeTask():
    
    if(tasks.getNumTasks() > 0): 
        task = tasks.getNextTask()
      
        if task.action == "i": 
            insertInTxt("prueba.txt",task.pointer,task.content)
        elif task.action =="d":
            ereaseInTxt("prueba.txt",task.pointer,task.repetitions)
        tasks.nextTaskCompleted()
    sleep(PERIOD)

def taskExecution():
    while True:
        executeTask()
        
def encrypt (msg):
    res=[]
    i=0
    for elem in msg:
        elem =str(elem)
        res.append("")
        for l in elem:
            res[i]+=chr(KEY+ord(l))
        i+=1
    
    return res

def decrypt(text):
    res=[]
    i=0
    for elem in msg:
        elem =str(elem)
        res.append("")
        for l in elem:
            res[i]+=chr(KEY+ord(l))
        i+=1
    
    return res


def start():
    thread = threading.Thread(target=taskExecution)
    
    thread.start()
    server.listen()
    
    clients = 0
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=listen, args=(conn, addr, clients))
        thread.start()
        clients += 1




start()
