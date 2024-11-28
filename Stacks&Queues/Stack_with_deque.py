from collections import deque

stack = deque()

stack.append(0)
stack.append(1)
stack.append(2)
stack.append(3)
stack.append(4)  # last in = 4
print(stack.pop())  # = 4 --> first out


