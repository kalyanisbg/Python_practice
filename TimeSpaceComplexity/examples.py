'''
TASK: Find first duplicate value
--------------------------------
Given an array of int between 1 and n, where n is the length of array, write a function that returns
the first int that appears more than once (when we read array left to right)
If no integer appears more than once, then we return -1.
'''

def first_duplicate_value0(array):
    for i, item in enumerate(sorted(array)):
        if i == len(array) - 1:
            return -1
        elif sorted(array)[i] == sorted(array)[i+1] and i < len(array) - 1:
            return item

# print(first_duplicate_value([3, 5, 1, 2, 3, 4, 3, 7]))
# print(first_duplicate_value([2, 5, 3]))

# Time complexity
# sorting an array takes O(nlogn) where n is the length of the array
# looping through the array has a time complexity of O(n)
# Because the sorting is nested in the looping (i.e., they are not independent sequential), O(n) x O(nlogn) = O(n^2logn)

# Space complexity
# sorted() function creates a new sorted list, which requires additional space proportional to the size of the input array
# O(n)

def first_duplicate_value1(array):
    sorted_array = sorted(array)
    for i, item in enumerate(sorted_array):
        if i == len(array) - 1:
            return -1
        elif sorted_array[i] == sorted_array[i+1] and i < len(array) - 1:
            return item
        
# Time
# sorted contributes O(nlogn)
# loop contributes O(n)
# since sorting and looping is independent sequential in this case, we ADD them together rather than multiply
# O(nlogn) + O(n) but O(nlogn) >>> O(n), therefore, time complexity is just O(nlogn)

# Space
# O(n)

def first_duplicate_value2(array):
    array.sort()
    for i, item in enumerate(array):
        if i == len(array) - 1:
            return -1
        elif array[i] == array[i+1] and i < len(array) - 1:
            return item

# print(first_duplicate_value2([3, 5, 1, 2, 3, 4, 3, 7]))
# print(first_duplicate_value2([2, 5, 3]))

# Time
# Sorting an array takes O(nlogn)
# iterating over an array takes O(n)
# O(nlogn) + O(n) = O(nlogn)

# Space O(1)

def first_dupe_value3(list):
    min_second_idx = len(list)

    for i in range(len(list)):
        value = list[i]
        for j in range(i + 1, len(list)):
            value_to_compare = list[j]
            if value == value_to_compare:
                min_second_idx = min(min_second_idx, j)
    if min_second_idx == len(list):
        return -1
    return list[min_second_idx]

# Time
# loop inside a loop = O(n^2)

# Space
# No new data structures creates, therefore, O(1)

def first_dupe_value4(array):
    seen = set()
    for val in array:
        if val in seen:
            return val
        seen.add(val)
    return -1

# Time
# There is only one loop, which means the more elements array has, the more time it is going to take, i.e., proportional to number of elements, so, O(n)

# Space
# a new datastructure is created (seen) and values are being appended with each iteration. Since the number of iterations is equal to the length of the array, O(n)

def first_dupe_value5(array):
    for val in array:
        abs_val = abs(val)
        if array[abs_val - 1] < 0:
            return abs_val
        # make that value negative by multiplying to -1
        array[abs_val - 1] *= -1
    return -1

# Time
# O(n)

# Space
# O(1) since no new data structures are created

def print_first_item(items):
    print(items[0])

# Time O(1)
# Space O(1)

def print_all_items(items):
    for item in items:
        print(item)

# Time O(n)
# Space O(1)

def print_all_items_twice(items):
    for item in items:
        print(item)
    for item in items:
        print(item)

# Time O(n)
# Space O(1)

def print_all_possible_ordered_pairs(items):
    for first_item in items:
        for second_item in items:
            print(first_item, second_item)

# Time O(n^2)
# Space O(1)