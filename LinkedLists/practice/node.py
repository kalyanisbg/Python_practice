'''
A node is where the data lives. Each node is composed of two things: data and links to the
linked node
'''
class Node:
    def __init__(self, value, next_node=None):
        self.set_value(value)
        self.set_next_node(next_node)

    def set_value(self, value):
        self.__value = value

    def get_value(self):
        return self.__value

    def set_next_node(self, next_node):
        self.__next_node = next_node

    def get_next_node(self):
        return self.__next_node



yacko = Node('likes to look at coconut trees')
wacko = Node(54)
dot = Node(True)

yacko.set_next_node(dot)
dot.set_next_node(wacko)

wackos_value = dot.get_next_node().get_value()
print(wackos_value)