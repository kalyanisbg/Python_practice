**Question 1**
collections

**Question 2**
In both trees and graphs, we have nodes (which holds data) and edges (links) connecting the nodes part of the tree/graph
- In trees, data moves down from one node to the other (vertical movement) whereas in graphs, data can move both vertically and horizontally. For this reason, trees are usually preferred to store hierarchical data with a directed flow. Whereas graphs can be either directed or undirected. So, in a way a tree can be thought of as a special type of graph
- In trees, we have the concepts of parent, children and root reflecting the hierarchical nature of the data they represent. There is always a single 'root' (master parent if you will) that all other nodes 'descend' from. Each node can only have a single parent and the nodes can't be linked in cycles (you always see a hierarchy - something descending from the other). Whereas in graphs, we don't have the concept of a 'root'. The concept of a 'parent' is not really relevant in graphs and there are no limitations on how many other nodes a given node can be connected to (as opposed to the strict only one parent restriction in trees, note that in trees a single node can still have multiple children but not more than one parent). So in graphs there is no restriction on how nodes can connect to each other

**Question 3**
- Time complexity of an algorithm is a way to quantify its efficiency based on the amount of time it takes to run as a function of the input size
- Space complexity is a way to quantify the efficiency based on the memory an algorithm uses as a function of the input size
- They are both denoted using the big O notation O(n), O(n^2), O(log n) etc where n is the input size (eg: length of a input list)

**Question 4**
- Bubble sort algorithm compares adjacent elements by iterating through an iterable (usually a list) and make constant swaps until you reach the desired goal. Bubble sort algorithms usually have 2 for loops which results in an O(n^2) time complexity for a list of size n. Depending on the creation of new data structures, the space complexity can vary. If we manage to come up with a code which doesn't create any new data structures, we would be able to achieve the ideal O(1) space complexity. Depending on the type of sort, after the first pass (means after the first full cycle of the big loop), the smallest number/element would be at the first or last position of the list

**Question 5**
- LIFO = Last In First Out: It is when in a data structure the last element to be added is removed first. Eg: stacks
Lists are classic examples of stacks
``` Python
my_list_stack = []

my_list_stack.append(1)
my_list_stack.append(2)
my_list_stack.append(3)
my_list_stack.append(4) # this is the last element to be added, aka 'Last In'

print(my_list_stack.pop())  # prints 4 as .pop() removes 4 and returns it, which means 4 is the first element to be removed, aka 'First Out'
```
- FIFO = First In First Out: It is when the first element to be added is the first to be removed. Eg: Queues: deques with popleft functionality is an example of a queue implementation

``` Python
from collections import deque

queue = deque()

queue.append(1)  # First element to be added, aka 'First In'
queue.append(2)
queue.append(3)
queue.append(4)

print(queue.popleft())  # prints 1 => the first element to be removed, aka 'First Out'
```

**Question 6**
A binary tree is a special type of tree where each node has upto two children - a left child/subtree or a right child/subtree or both. A balanced binary tree is when the left and right subtrees of each node differ in height (no: of edges till the leaf) by no more than 1. Therefore the maximum difference in height between the left and right subtrees should be 1. Which is to say that, in a binary tree the difference in height between the left and right subtrees of any node should be either 1 or 0. So, any node in a binary tree, where this difference is 0 (minimum) would be the best.

``` Python
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, new_data):
        # Compare the new value to the parent node
        if self.data:
            if new_data <= self.data:
                if self.left is None:
                    self.left = Node(new_data)
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
                return f'{value} is not found'
            return self.left.find_value(value)
        elif value > self.data:
            if self.right is None:
                return f'{value} is not found'
            return self.right.find_value(value)
        else:
            return f'{value} exists in the list'

    def sum_of_leaves(self):
        if self.left is None and self.right is None:
            return self.data

        leaf_sum = 0
        if self.left is not None:
            leaf_sum += self.left.sum_of_leaves()
        if self.right is not None:
            leaf_sum += self.right.sum_of_leaves()

        return leaf_sum


root = Node(27)
root.insert(14)
root.insert(35)
root.insert(31)
root.insert(10)
root.insert(9)
root.insert(11)

print(root.sum_of_leaves())
```
In this code when we insert 14 to the root, since it is less than 27, it goes to the left child node. Since the left child node is vacant at the start, 14 becomes the left child node. Next when we insert 35, since 35 is greater than 27, it goes to the right child node, which is vacant and is filled by 35. After that 31, which is again greater than 27, goes to the right child subtree where it meets 35. Since 31 is less than 35, it goes to 35's left child subtree. Since 35 doesn't have a left child node, 31 becomes 35's left child node. Then we insert 10 which goes to the the left subtree of both 27 and 14 where it finds that 14's left child node is empty. So 10 becomes 14's left child. Similarly 9 become 10's left child and 11 becomes 10's right child. So at the bottom of the tree we have 9, 11 and 31.

The `find_value()` method in the given code demonstrates how searching for a value in a binary tree works. We compare the value we want to find to the value of the current node, if they are equal, yay, our search is successful! if the value we're after is less than the current node value, we go to the left subtree, otherwise we go to the right subtree. The process is done recursively at each node until we find a match. If we get to all the leaves and there is still no match, then the value we're looking for doesn't exist in the tree. 