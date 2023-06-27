'''
queue - a abordagem ao objeto
'''
class QueueError(IndexError):
    pass

class Queue: # Defining the Queue class
    def __init__(self):
        self.__queue = []

    def is_empty(self):
        return len(self.__queue) == 0

    def put(self, ele):
        self.__queue.append(ele)

    def get(self):
        if self.is_empty():
           raise QueueError('Error: empty queue')
         
        ele = self.__queue[0]
        del self.__queue[0]
        return ele 

    def clear(self):
        self.__queue.clear()

    def head(self):
        return self.__queue[0]

    def tail(self):
        return self.__queue[-1]
    

if __name__ == '__main__':
    que = Queue()
    que.put(1)
    que.put("dog")
    que.put(False)
    try:
        for i in range(4):
            print(que.get())
    except QueueError:
        print("Queue error")
