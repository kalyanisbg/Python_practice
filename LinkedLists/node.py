'''
NODE
- where data is stored in a linked list
- each node also holds a pointer, which is a reference to the next node in the list
'''

class Node:
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

   def get_data(self):
        return self.data

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next