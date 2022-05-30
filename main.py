from ast import While
from sqlite3 import Time
from black import schedule_formatting
import eel
from numpy import block
import time
from client import *
from Tasks import *
from threading import Timer
import time


period = 0.5
lastPointer = 0
tasks = Tasks()

def resetVariables():
    pass


def sendLoop():
    while True:
        sendTasks()
        sleep(period)
    

def sendTasks():
    while(tasks.getNumTasks()>0):   
        print("NUMERO DE TAREAS A ENVIAR ------------------ ",tasks.getNumTasks(), tasks.getNextTask().toArray())
        print(tasks.getNumTasks())
        
        sendMsg(tasks.getNextTask().toArray())
        tasks.nextTaskCompleted()
        resetVariables()


@eel.expose
def erease(pointer,action):
    global lastPointer
    print("erease---------->",pointer)

    if(not tasks.AreTheretTasksOfType(action)):
        task = Task([pointer,action,"",1])
        tasks.addTask(task) 
    else:
        if pointer == lastPointer-1:
            print("se borra de forma secuencial",tasks.getNextTask().content)
            tasks.getNextTask().amount += 1
        else:
            task = Task([pointer,action,"",1])
            tasks.addTask(task)   
            tasks.getNextTask().print()
    lastPointer = pointer 


@eel.expose
def edit(action,pointer,text):
    global lastPointer
    print("insert---------->",text)

    if(not tasks.AreTheretTasksOfType(action)):
        task = Task([pointer,action,text,0])
        tasks.addTask(task) 
    else:
        if pointer == lastPointer+1:
            print("se escribe de forma secuencial", pointer, " ", lastPointer)
            tasks.getNextTask().content += text
            
        else:
            task = Task([pointer,action,text,0])
            tasks.addTask(task)   
            tasks.getNextTask().print()


    lastPointer = pointer 

thread = threading.Thread(target=sendLoop)
thread.start()
eel.init('web')
eel.start('./templates/index.html', mode='chrome-app', port=8080, cmdline_args=['--start-fullscreen', '--browser-startup-dialog'])

