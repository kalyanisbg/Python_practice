class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def insert(self, new_data):
        # compare the new value to the parent node
        if self.data: # checking if parent node data exists
            if new_data <= self.data:
                if self.left is None:
                    self.left = Node(new_data)  # creating a new node with data
                else:
                    self.left.insert(new_data)
            elif new_data > self.data:
                if self.right is None:
                    self.right = Node(new_data)
                else:
                    self.right.insert(new_data)
        else:
            self.data = new_data

    def find_value(self, value):
        if value < self.data:
            if self.left is None:
                return f"{value} is not found"
            return self.left.find_value(value)
        elif value > self.data:
            if self.right is None:
                return f"{value} is not found"
            return self.right.find_value(value)
        else:
            return f"{value} exists in the list"

    def sum_of_leaves(self):
        if self.left is None and self.right is None:
            return self.data
        leaf_sum = 0
        if self.left:
            leaf_sum += self.left.sum_of_leaves()
        if self.right:
            leaf_sum += self.right.sum_of_leaves()
        return leaf_sum