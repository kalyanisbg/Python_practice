'''
Create a StackList class that implements a stack data structure using a list. The class should have the following methods:
	1.	__init__(self, size): Initialize the stack with a given size. Set the initial stack to be empty, and track the top index.
	2.	push(self, x): Add an element to the top of the stack. If the stack is full, print a message and prevent further additions.
	3.	pop(self): Remove and return the top element from the stack. If the stack is empty, print a message and prevent removal.
	4.	is_full(self): Return True if the stack is full, otherwise return False.
	5.	is_empty(self): Return True if the stack is empty, otherwise return False.

Test the StackList class by creating an object with a defined size, pushing elements onto the stack, and popping them off while observing the correct behavior.
'''

class StackList:
    def __init__(self, size):
        self.size = size
        self.top_index = -1  # initially there are no elements in the stack so the stack is empty
        self.stack = [None] * size

    def push(self, x):
        if self.is_full():
            print("The list is full")
            exit()
        self.top_index += 1
        self.stack[self.top_index] = x

    def pop(self):
        if self.is_empty():
            print("The list is empty, nothing to pop")
            exit()
        # fetch the current top element
        top_element = self.stack[self.top_index]
        # delete the current top element by setting it to None
        self.stack[self.top_index] = None
        # update the top_index
        self.top_index -= 1
        return top_element

    def is_full(self):
        return self.top_index + 1 == self.size
    
    def is_empty(self):
        return self.top_index == -1


my_stack_list = StackList(3)  # [None, None, None]
my_stack_list.push(78)
print(my_stack_list.stack[0])
print(my_stack_list.stack)
my_stack_list.push(92)
print(my_stack_list.stack)
my_stack_list.push("red peppers")
print(my_stack_list.stack)
# my_stack_list.push("infinity")
my_stack_list.pop()
print(my_stack_list.stack)
my_stack_list.pop()
print(my_stack_list.stack)
my_stack_list.pop()
print(my_stack_list.stack)
my_stack_list.pop()