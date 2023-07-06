'''
Managment of a task
'''

from datetime import datetime
from enum import Enum
from timestamp import Timestamp

class TaskError(UserWarning):
    pass

class Priority(Enum):
    LOW = 0
    NORMAL = 1
    HIGH = 2

class Category:
    def __init__(self, id, name):
        self.__id = id
        self.set_name(name)
    
    def __str__(self):
        return '(' + str(self.get_id()) + ' - '+ self.get_name() + ')'
    
    def get_id(self):
        return self.__id
    
    def set_name(self, name):
        if len(name) == 0:
            raise TaskError("Error: Category can't be blank")
        self.__name = name
    
    def get_name(self):
        return self.__name
    
class Task:
    __task_num = 0
    def __init__(self, design):
        self.set_design(design)
        Task.__task_num += 1
        self.__id = Task.__task_num

        now = datetime.now()
        self.__conclusion = datetime(now.year, now.month, now.day, hour=23, minute=59)

        self.__timestamps = []

        self.__timestamp = None
        self.__elapsed_time = 0.0

        self.__category = None
        self.__priority = Priority.NORMAL
        self.__completed = False


    def get_id(self):
        return self.__id

    def get_design(self):
        return self.__design       

    def set_design(self, text):
        if len(text) == 0:
            raise TaskError('Error: designation is empty')
        self.__design = text

    def __str__(self):
        return str(self.get_id()) + ' - ' + self.get_design() + ' - ' + str(self.__conclusion) \
            + ' - ' + str(self.get_category()) \
            + ' - ' + str(self.__priority) + ' - ' + str(self.__completed) + ' - ' + str(self.__elapsed_time) + ' s'

    def start(self):
        if self.__timestamp != None:
            raise TaskError('Error: clock is already running')
         
        self.__timestamp = Timestamp()
        
    def stop(self):
        if self.__timestamp is None:
            raise TaskError('Error: clock not started')
        
        self.__timestamp.set_end(datetime.now())
        self.__elapsed_time += self.__timestamp.get_secs()

        self.__timestamps.append(self.__timestamp)

        self.__timestamp = None

    def isClockRunning(self):
        return self.__timestamp != None

    def isCompleted(self):
        return self.__completed
    
    def complete_task(self):
        if self.isCompleted():
            raise TaskError('Error: Task already completed')
        
        if self.isClockRunning(): 
            self.stop()
        self.__completed = True
    
    def get_timestamps(self):
        return self.__timestamps[:]

    def set_category(self, category):
        self.__category = category

    def get_category(self):
        return self.__category
    
if __name__ == '__main__':
    import time
    import random

    aTask = None
    try:
        aTask = Task('') # create a 1st task and add to task list 
    except TaskError as e:
        print(aTask, e)
        aTask = Task('My first task') # create a 1st task and add to task list 
    aTask.start()
    
    time.sleep(random.randint(0,5)) # random value between 0 and 5 seconds

    otherTask = Task('My second task') # create a 2nd task and add to task list
    otherTask.set_category(Category(1, 'Professional tasks'))
    otherTask.start()

    time.sleep(random.randrange(0,5,2)) # random value from 0, 2, 4 range
    anotherTask = Task('My third task ') # create a 3rd task and add to task list

    try:
        aTask.start()
    except TaskError as e:
        print('Task error!!!:', e) # , traceback.format_exc(), sep='\n'

    aTask.stop()
    time.sleep(random.randrange(0,5)) # random value from 0, 2, 4 range
    aTask.start()
    time.sleep(random.randrange(0,5)) # random value from 0, 2, 4 range
    aTask.stop()
    aTask.start()

    otherTask.stop()
    time.sleep(random.randrange(0,2)) # random value from 0, 2, 4 range
    aTask.complete_task()

    try:
        anotherTask.stop()
    except TaskError as e:
        print(e) # , traceback.format_exc(), sep='\n'

    print('1st task:', aTask, sep='\n\t')
    for time_rec in aTask.get_timestamps():
        print('\t\t', time_rec)
    print('2nd task:', otherTask, sep='\n\t')
    for time_rec in otherTask.get_timestamps():
        print('\t\t', time_rec)
    print('3rd task:', anotherTask, sep='\n\t')
    for time_rec in anotherTask.get_timestamps():
        print('\t\t', time_rec)
