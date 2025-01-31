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


class LinkedList:
    def __init__(self, value=None):
        self.head_node = Node(value)

    def get_head_node(self):
        return self.head_node


def traversal(linked_list, val1, val2):
    node = linked_list.get_head_node()
    node_1 = None
    node_2 = None
    while node:
        if node.get_value() == val1:
            node_1 = node
        elif node.get_value() == val2:
            node_2 = node
        node = node.get_next_node()
    return node_1, node_2


def swap(node_1, node_2):
    if node_1 != node_2:
        val1_old = node_1.get_value()
        val2_old = node_2.get_value()
        node_1.set_value(val2_old)
        node_2.set_value(val1_old)
        return node_1, node_2


def swap_nodes(linked_list, val1, val2):
    node_1, node_2 = traversal(linked_list, val1, val2)
    if node_1 and node_2:
        swap(node_1, node_2)
    else:
        print("One or more nodes not found")
    return linked_list


