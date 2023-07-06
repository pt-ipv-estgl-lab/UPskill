'''
Managment timestamps
'''
from datetime import datetime

class TimeError(UserWarning): # Time Errors 
    pass

class Timestamp:
    def __init__(self, begin=None, end=None): # Constructor
        self.__begin = None
        self.__end = None
        if begin == None: begin = datetime.now()
        self.set_begin(begin)
        self.set_end(end)

    def __str__(self):                                  # textual representation of a timestamp
        return str(self.get_begin()) + ' -> ' + str(self.get_end()) + ' = ' + str(self.get_secs()) + ' s'

    def get_begin(self):
        return self.__begin
    
    def set_begin(self, moment = datetime.now()):
        if self.__end != None and moment > self.__end: 
            raise TimeError('Error: begin time after end time')
        self.__begin = moment     

    def get_end(self):
        return self.__end
    
    def set_end(self, moment = datetime.now()):
        if self.__begin == None:  
            raise TimeError('Error: begin time is None')
        if self.__end != None and moment < self.__begin:
            raise TimeError('Error: end time before begin time')
        
        self.__end = moment
    
    def get_secs(self):
        if self.__begin == None or self.__end == None:
            raise TimeError('Error: None on begin or end time')         
        return (self.__end - self.__begin).total_seconds()

if __name__ == '__main__': # for testing propose
    import time
    import random

    time_record = Timestamp()
    time.sleep(random.randint(0,5))

    time_record.set_end(datetime.now())

    print('time record:', time_record)
    try:
        print('elapsed:', time_record.get_secs(), 'secs')
    except TimeError as e:
        print(e)