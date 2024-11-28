from collections import deque

'''
1. Queue Implementation
Implement a queue using deque with the following operations:
- enqueue(item): Add an item to the end of the queue.
- dequeue(): Remove and return the item at the front of the queue.
- peek(): Return the front item without removing it.
- is_empty(): Check if the queue is empty.
'''

'''
2. Stack Implementation Using Deque
Implement a stack using deque with the following operations:
- push(item): Add an item to the top of the stack.
- pop(): Remove and return the top item from the stack.
- peek(): Return the top item without removing it.
- is_empty(): Check if the stack is empty.
'''
'''
3. Sliding Window Maximum
Given a list of integers and a window size, find the maximum element in each window.
Use a deque to store indices of the array elements and maintain the order for each sliding window.

Example input: nums = [1, 3, -1, -3, 5, 3, 6, 7], window_size = 3
Expected output: Maximums in each window.
'''

def sliding_window_maximum(int_list, window_size):
    # a deque to store the window
    # a list to store the maximums
    # starting at int_list[3], popleft and append(int_list[3])
    # max(deque) at each step and append to list of maximums
    # return max list
    max_list = []
    for i in range(len(int_list)-window_size+1):
        window = int_list[i:i+window_size]
        max_list.append(max(window))
    return max_list

# Time O(n * window_size) Space O(n)

# print(sliding_window_maximum([1, 3, -1, -3, 5, 3, 6, 7], 3))

'''
4. Palindrome Checker Using Deque
Implement a function to check if a given string is a palindrome using deque.
- A palindrome is a string that reads the same forward and backward.
Example input: "racecar"
Example output: True
'''

# odd number of letters - check if middle index +- (len(string)-1)/2 are the same, the first time its not give False
# even numbers - i = 0 to len(string)/2 - 1 and -(i+1) the same? the first time its not give False

# without using deque
def is_palindrome(string):
    if len(string)%2 != 0:
        mid_index = int((len(string) - 1)/2)
        for i in range(int((len(string)-1)/2)):
            if string[mid_index + i] != string[mid_index - i]:
                return False
    else:
        for i in range(int(len(string)/2) - 1):
            if string[i] != string[-(i+1)]:
                return False
    return True

# Time O(n) Space O(1)

# using deque
def is_palindrome_using_deque(string):
    deq = deque()
    for i in string:
        deq.append(i)
    for j in range(len(string)):
        if deq[j] != deq[-(j+1)]:
            return False
    return True

# Time O(n) Space O(n)

print(is_palindrome_using_deque("racecar"))
print(is_palindrome_using_deque("emma"))
'''
5. Task Scheduler Using Deque
You have a set of tasks to execute, and each task requires a certain amount of time. 
Implement a function that simulates the scheduling of these tasks using a deque:
- Each task can either be completed in the given time or remain in the deque if it's not finished.
- Use a deque to manage the tasks and execute them in order.
'''



'''
6. Removing Even Numbers
Create a program that removes all even numbers from a deque:
- Iterate through a deque and remove any even numbers.
- Return the updated deque.
Example input: deque([1, 2, 3, 4, 5, 6])
Expected output: deque([1, 3, 5])
'''
'''
7. Rotating a Deque
Implement a function that rotates a deque by a given number of positions.
- Positive numbers should rotate to the right, and negative numbers should rotate to the left.
Example input: deque([1, 2, 3, 4, 5]), rotate by 2
Expected output: deque([4, 5, 1, 2, 3])
'''
'''
8. Merge Two Deques
You are given two deques of integers. Implement a function to merge these two deques into one.
- Maintain the order of elements in both deques.
Example input: deque([1, 3, 5]), deque([2, 4, 6])
Expected output: deque([1, 3, 5, 2, 4, 6])
'''
'''
9. Deque from Left and Right
Create a program that adds elements to both ends of a deque:
- Add items to the left using appendleft.
- Add items to the right using append.
Example input: deque([1, 2, 3]), appendleft(0), append(4)
Expected output: deque([0, 1, 2, 3, 4])
'''
'''
10. Deque Reversal
Implement a function that reverses the elements of a deque:
- Use deque's inherent properties to reverse the deque without using additional data structures.
Example input: deque([1, 2, 3, 4])
Expected output: deque([4, 3, 2, 1])
'''