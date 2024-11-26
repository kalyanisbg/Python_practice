class MyQueue:
    def __init__(self, size):
        self.q = [None] * size
        self.capacity = size
        self.front = 0  # First element index
        self.rear = -1  # Last element index
        self.count = 0

    def pop(self):
        if self.is_empty():
            print("There is nothing to pop")
            exit(1)
        print(f"Removing element {self.q[self.front]} from the queue")
        self.front = (self.front + 1) % self.capacity
        self.count = self.count - 1

    def size(self):
        return self.count

    def is_empty(self):
        return self.size() == 0

    def is_full(self):
        return self.size() == self.capacity()