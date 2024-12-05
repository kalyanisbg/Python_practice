from collections import deque

our_queue = deque()

our_queue.append(1)
our_queue.append(2)
our_queue.append(3)

print(our_queue)

element = our_queue.popleft()
print(f'removing element {element}')
print(our_queue)