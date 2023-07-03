'''
Managment of my tasks
'''
from datetime import datetime
from enum import Enum

class TaskError(RuntimeWarning):
    pass

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
        self.__elapsed_time = 0.0

        self.start() # beginning count of elapsed time 

        self.__categories = []
        self.__priority = Priority.NORMAL
        # ...
        self.__completed = False
    

    def start(self):
        if self.__start_time != None:
            raise TaskError('Error: clock is already running')
         
        self.__start_time = datetime.now()
        
    def stop(self):
        if self.__start_time is None:
            raise TaskError('Error: clock not started')
        
        self.__elapsed_time += (datetime.now() - self.__start_time).total_seconds()

        self.__start_time = None



    def __str__(self):
        return str(self.__id) + ' - ' + self.__design + ' - ' + str(self.__conclusion) \
        +' - ' + str(self.__categories) \
            + ' - ' + str(self.__priority) + ' - ' + str(self.__completed) + ' - ' + str(self.__elapsed_time)
    
   
    def isClockRunning(self):
        return self.__start_time != None

    def isCompleted(self):
        return self.__completed
    
    def complete(self):
        if self.isCompleted():
            raise TaskError('Error: Task already completed')
        
        if self.isClockRunning(): self.stop()
        self.__completed = True
    
        
if __name__ == '__main__':
    import time
    import traceback

    aTask = Task('My first task')
    otherTask = Task('Nothing to do...')
    print('a Task:', aTask)
    print('a Task:', otherTask)

    time.sleep(2)
    try:
        aTask.start()
    except TaskError:
        print('Task error!!!:', traceback.format_exc(), sep='\n')

    aTask.stop()
    time.sleep(3)
    aTask.start()

    aTask.complete()
    otherTask.complete()
    print('a Task:', aTask)
    print('a Task:', otherTask)

