'''
 A stack - a abordagem processual

'''
__stack = []

def push(__stack, val):
    __stack.append(val)

def pop(__stack):
    val = __stack[-1]
    del __stack[-1]
    return val
    # return stack.pop()

def erase(__stack):
    __stack.clear()

def top(__stack):
    return __stack[-1]

def is_empty(__stack):
    return len(__stack) == 0

if __name__ == '__main__':
    push(__stack, 1)
    push(__stack, 2)
    push(__stack, 3)

    print(__stack)

    print('on top of stack:', top(__stack))

    print(pop(__stack))
    print(pop(__stack))
    print(pop(__stack))
    print('Is stack empty?', is_empty(__stack))
    # print(pop())
