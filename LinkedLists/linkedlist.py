from node import Node

'''
LINKED LIST
The following implementation includes the following methods:
- Insert: inserts a new node into the list
- Size: returns size of list
- Search: searches list for a node containing the requested data and returns that node if found
- Delete: seraches list for a node containing the requested data and removes it from the list if found
'''

class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            node.append(str(node.data))
            node = node.next_node
        node.append('None')
        return '->'.join(nodes)

    def insert(self, data):
        new_node = Node(data)
        new_node.set_next(self.head)

    def size(self):
        pass

    def search(self, data):
        pass

    def delete(self, data):
        pass
