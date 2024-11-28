import itertools

"""
Exercise 1: Infinite Counter with Stop Condition
Task: Use itertools.count to create an infinite counter starting from 10, incrementing by 2. 
Stop and print values only up to 20.
Hint: Use a for loop with a break condition.

Expected Output:
10
12
14
16
18
20
"""

# generate an iterator
iterator = itertools.count(start=10, step=2)
# if number is <= 20, print
for number in iterator:
    if number <= 20:
        print(number)
    else:
        break
# else break

"""
Exercise 2: Generating Sequential Keys
Task: Use itertools.count to generate sequential IDs starting from 1 for a list of names.
Example Input: ["Alice", "Bob", "Charlie"]
Expected Output:
1: Alice
2: Bob
3: Charlie
"""

# generate an iterator
# for loop to limit count
# loop through the list
# print

iterator1 = itertools.count(start=1)
names = ["Alice", "Bob", "Charlie"]
for num in iterator1:
    if num <= len(names):
        print(f"{num}: {names[num - 1]}")
    else:
        break