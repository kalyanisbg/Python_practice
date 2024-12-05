"""
TASK
Find the length of a linked list.
A user should enter the elements of the linked list to create and then displays its length.

Steps:
- Create a class Node
- Create a class LinkedList
- Define method append inside the class LinkedList to append data to the linked list
- Define method length
- The method length uses a loop to iterate over the nodes of the list to calculate its length
- Create an instance of LinkedList and prompt the user for its elements
- Display the length of the list by calling the method length


"""


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


class LinkedList():
    def __init__(self):
        pass

    def append(self, data):
        
