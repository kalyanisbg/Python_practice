class StackList:
    def __init__(self, size):
        self.container = [None] * size
        self.capacity = size
        self.top = -1  # because we push to and pop out of the last index
    def push(self, x):
        '''
        Method to add an element to the stack
        '''
        if self.is_full():
            print("The list is full. You cannot add anything")
            exit()
        print(f'Inserting {x} into the stack')  #   LOGGING
        self.top += 1 # initially 0
        self.container[self.top] = x # establishes the first element as x 

    def pop(self):
        '''
        Method of return and remove the top element from the stack
        '''
        if self.is_empty():
            print("Stack is empty. Cannot pop")
            exit()
        print(f"Returning top of the stack")
        top_element = self.container[self.top]  # self.container[-1] last element is popped first
        self.top -= 1
        self.container[self.top] = None
        return top_element

    def is_full(self):
        return self.capacity == self.top + 1

    def is_empty(self):
        return self.capacity == -1

# Examples of functionality
stack = StackList(3)
print(stack)  # [None, None, None]
stack.push(1)
print(stack[0])
