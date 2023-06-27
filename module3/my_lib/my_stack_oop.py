'''
stack - a abordagem ao objeto
'''
class Stack: # Defining the Stack class
    def __init__(self):
        self.__stack = []

    def push(self, val):
        self.__stack.append(val)

    def pop(self):
        val = self.__stack[-1]
        del self.__stack[-1]
        return val # return self.__stack.pop()

    def erase(self):
        self.__stack.clear()

    def top(self):
        return self.__stack[-1]

    def is_empty(self):
        return len(self.__stack) == 0

if __name__ == '__main__':
    my_stack_object = Stack()   # Instantiating an object
    print(my_stack_object.is_empty())
    my_stack_object.push('A')
    print(my_stack_object.is_empty())
    my_stack_object.push('B')
    my_stack_object.push('C')
    print(my_stack_object.pop())
    print(my_stack_object.pop())
    print(my_stack_object.pop())

