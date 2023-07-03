'''
Managment of my tasks
'''
from datetime import datetime
from enum import Enum
import time

class Priority(Enum):
    LOW = 0
    NORMAL = 1
    HIGH = 2

class Task:
    __task_num = 0
    def __init__(self, design):
        Task.__task_num += 1
        self.__id = Task.__task_num
        self.__design = design
        now = datetime.now()
        self.__conclusion = datetime(now.year, now.month, now.day, hour=23, minute=59)
        
        #datetime(int(datetime.year), int(datetime.month), int(datetime.day),hour=23,minute=59)
        self.__start_time = None
        self.__elapsed_time = None       
        self.start()

        self.__categories = []
        self.__priority = Priority.NORMAL
        # ...
        self.__completed = False
    

    def start(self):
        self.__start_time = datetime.now()
        #print(self.__start_time)

    def stop(self):
        if self.__start_time is None:
            print("Task not started yet.")
            return
        
        self.__elapsed_time = datetime.now() - self.__start_time

        self.__start_time = None



    def __str__(self):
        return str(self.__id) + ' - ' + self.__design + ' - ' + str(self.__conclusion) \
        +' - ' + str(self.__categories) \
            + ' - ' + str(self.__priority) + ' - ' + str(self.__completed) + ' - ' + str(self.__elapsed_time)
    
   


    def isCompleted(self):
        return self.__completed
    
    def complete(self):
        self.__completed = True
        self.stop()
    
        
if __name__ == '__main__':
    aTask = Task('Nothing')
    otherTask = Task('Nothing to do...')
    print('a Task:', aTask)
    print('a Task:', otherTask)

    time.sleep(4)
    aTask.complete()
    otherTask.complete()
    print('a Task:', aTask)
    print('a Task:', otherTask)

