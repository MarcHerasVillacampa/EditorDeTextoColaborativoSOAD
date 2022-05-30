from asyncio import tasks
import time


class Tasks:
    taskList = []
    
    def __init__(self, tasks):
        self.taskList=tasks
    
    def __init__(self):
        self.taskList=[]
    
    def addTask(self,task):
        self.taskList.append(task)
    
    def delTask(self,task):
        self.taskList.pop(0)

    def append(self,task):
        self.taskList.append(task)

    def getNumTasks(self):
        return len(self.taskList)
    
    def nextTaskCompleted(self):
        self.taskList.pop(0)

    def getNextTask(self):
        if len(self.taskList) <=0:
            return
        return self.taskList[0]

    def AreTheretTasksOfType(self,type):
        for t in self.taskList:
            if t.action == type:
                return True
        return False


class Task:
    # id=''
    path=''
    action =''
    content=''
    pointer=''
    repetitions =''
    timestamp=''

    def __init__(self,id,path,action,content):
        # self.id = id
        self.path=path
        self.action=action
        self.content=content
    
    def __init__(self,args):
        # self.id = id
        self.pointer=args[0]
        self.action=args[1]
        self.content=args[2]
        self.repetitions=args[3]
        self.timestamp=time.time()
        # print(f"CONSTRUCTORA TASK {self.id}, {self.path}, {self.action}, {self.content}")
    
    # def __init__(self,args):
    #     # self.id = id
    #     self.pointer=args[0]
    #     self.action=args[1]
    #     self.amount=args[2]
    #     # self.timestamp=time.time()

    def getFile(self):
        return self.path

    def getAction(self):
        return self.action

    def getContent(self):
        return self.content
    
    def getPointer(self):
        return self.content

    def getTimestamp(self):
        return self.content

    def getID(self):
        return self.id

    def print(self):
        print("TASK: ",self.pointer, self.action, self.content, self.timestamp)

    
    def toArray(self):
        if self.action == "i":
            return [self.pointer, self.action, self.content, self.timestamp]
        else:
            return [self.pointer, self.action, self.content, self.repetitions]