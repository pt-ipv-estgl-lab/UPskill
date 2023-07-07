'''
Managment of a task list
'''
import task

class TaskList:
    def __init__(self):
        self.__tasks = []
    
    def create_task(self, task):
        self.__tasks.append(task)
    
    def on_going_tasks(self):
        on_going = []
        for task in self.__tasks:
            if not task.isCompleted():
                on_going.append(task)
        return on_going
    
    def completed_tasks(self):
        completed = []
        for task in self.__tasks:
            if task.isCompleted():
                completed.append(task)
        return completed

    def retrieve_task(self, id):
        for task in self.__tasks:
            if task.get_id() == id:
                return task
        return None

        
if __name__ == '__main__':
    import time
    import random

    my_tasks = TaskList() # create an empty task list 
    my_cats = [task.Category(1, 'Personal'), task.Category(2, 'Professional')] # two demo categories

    aTask = task.Task('My first task') # create a 1st task and add to task list 
    aTask.set_category(my_cats[0])
    aTask.start()
    my_tasks.create_task(aTask)
    
    aTask = task.Task('My second task') # create a 2nd task and add to task list
    aTask.start()
    my_tasks.create_task(aTask)

    aTask = task.Task('My third task ') # create a 3rd task and add to task list
    aTask.set_category(my_cats[1])
    my_tasks.create_task(aTask)

    aTask = task.Task('My fourth task ') # create a 4th task and add to task list
    aTask.set_category(my_cats[0])
    aTask.start()
    time.sleep(random.randint(1,3)) # random value between 1 and 3 seconds
    my_tasks.create_task(aTask)
    lastTask = my_tasks.retrieve_task(4)
    lastTask.stop()

    for the_task in my_tasks.on_going_tasks():
        print(the_task)
    print()

    time.sleep(random.randint(0,5)) # random value between 0 and 5 seconds
    try:
        aTask = my_tasks.retrieve_task(1) # retrieve 1st task
        aTask.start()
    except task.TaskError as e:
        print('Task error!!!:', e) # , traceback.format_exc(), sep='\n'

    aTask.stop()
    time.sleep(random.randrange(0,5)) # random value from 0, 2, 4 range
    aTask.start()
    time.sleep(random.randrange(0,5)) # random value from 0, 2, 4 range
    print('Ongoing tasks:')
    for a_task in my_tasks.on_going_tasks():
        print(a_task)
    print()
    aTask.complete_task()

    aTask = my_tasks.retrieve_task(2)
    aTask.stop()

    print('Completed tasks:')
    for a_task in my_tasks.completed_tasks():
        print(a_task)
        print('\tTimestamps:')
        for timestamp in a_task.get_timestamps():
            print('\t\t',timestamp)
    print()

    time.sleep(random.randint(0,5)) # random value between 0 and 5 seconds
    aTask = my_tasks.retrieve_task(3)
    try:
        aTask.stop()
    except task.TaskError:
        print('Task error!!!: Task not running') # , traceback.format_exc(), sep='\n'
    print()
    print('Now ongoing tasks:')
    for a_task in my_tasks.on_going_tasks():
        print(a_task)
        print()
    
    cat = 0
    print('Tasks of category:', my_cats[cat])
    for a_task in my_tasks.completed_tasks():
        if a_task.get_category() == my_cats[cat]:
            print('\t', a_task)
    for a_task in my_tasks.on_going_tasks():
        if a_task.get_category() == my_cats[cat]:
            print('\t', a_task)
