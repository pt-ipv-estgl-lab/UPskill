from sys import path
path.append('..\\my_lib')
# print(path)
import my_stack_p

stack1 = []
stack2 = []

my_stack_p.push(stack1,'A')
my_stack_p.push(stack1, 'B')
my_stack_p.push(stack1, 'C')

my_stack_p.push(stack2, 1.0)
my_stack_p.push(stack2, 2.0)


print('from stack1:', my_stack_p.pop(stack1))
my_stack_p.erase(stack1)

my_stack_p.push(stack1, 'B')
my_stack_p.push(stack1, 'C')

print('from stack2:', my_stack_p.pop(stack2))

my_stack_p.push(stack2, 3.0)

print('from stack1:', my_stack_p.pop(stack1))
print('from stack1:', my_stack_p.pop(stack1))
print('from stack2:', my_stack_p.pop(stack2))
print('from stack2:', my_stack_p.pop(stack2))

print('OOP:')
import my_stack_oop

stack1 = my_stack_oop.Stack()
stack2 = my_stack_oop.Stack()

stack1.push('A')
stack1.push('B')
stack1.push('C')

stack2.push(1.0)
stack2.push(2.0)


print('from stack1:', stack1.pop())
stack1.erase()

stack1.push('B')
stack1.push('C')

print('from stack2:', stack2.pop())

stack2.push(3.0)

print('from stack1:', stack1.pop())
print('from stack1:', stack1.pop())
print('from stack2:', stack2.pop())
print('from stack2:', stack2.pop())
