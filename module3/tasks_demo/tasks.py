'''
Managment of my tasks
'''
from datetime import datetime
from enum import Enum

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
        self.__conclusion = datetime(int(datetime.year), int(datetime.month), int(datetime.day),hour=23,minute=59)
        self.__categories = []
        self.__priority = Priority.NORMAL
        # ...
        self.__completed = False
    
    def __str__(self):
        return str(self.__id) + ' - ' + self.__design + ' - ' + str(self.__conclusion) \
            + ' - ' + str(self.__categories) \
            + ' - ' + str(self.__priority) + ' - ' + str(self.__completed)
    
    def isCompleted(self):
        return self.__completed
    
    def complete(self):
        self.__completed = True
    
        
if __name__ == '__main__':
    aTask = Task('Nothing')
    otherTask = Task('Nothing to do...')
    print('a Task:', aTask)
    print('a Task:', otherTask)

