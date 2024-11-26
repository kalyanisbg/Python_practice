from collections import OrderedDict

'''
1. Rearranging a Dictionary

Task: Write a program that takes a regular dictionary, rearranges its items in reverse insertion order, and converts it into an OrderedDict.

Example Input:
{'a': 1, 'b': 2, 'c': 3}

Example Output:
OrderedDict([('c', 3), ('b', 2), ('a', 1)])
'''

def get_ord_dict(dict):
    return OrderedDict(reversed(OrderedDict(dict).items()))

# print(get_ord_dict({'a': 1, 'b': 2, 'c': 3}))

'''
2. Counting Word Frequencies in Order

Task: Write a program that reads a string, splits it into words, and uses an OrderedDict to count the frequency of each word in the order of their first occurrence.

Example Input:
“apple banana apple orange banana apple”

Example Output:
OrderedDict([('apple', 3), ('banana', 2), ('orange', 1)])
'''

def word_freqs_in_order(string):
    words = string.split()
    freqs = OrderedDict()
    for word in words:
        if word in freqs:
            freqs[word] += 1
        else:
            freqs[word] = 1
    return freqs

# print(word_freqs_in_order("apple banana apple orange banana apple"))

'''
3. Sorting an OrderedDict

Task: Given an OrderedDict, write a program to sort it by its values (while keeping it as an OrderedDict).

Example Input:
OrderedDict([('a', 3), ('b', 1), ('c', 2)])

Example Output:
OrderedDict([('b', 1), ('c', 2), ('a', 3)])
'''

def sort_by_values(ord_dict):
    return OrderedDict(sorted(ord_dict.items(), key=lambda item:item[1]))

# print(sort_by_values(OrderedDict([('a', 3), ('b', 1), ('c', 2)])))

'''
4. Maintaining Insertion Order After Sorting

Task: Take a dictionary, sort it by values (as in Exercise 3), but store the sorted data back in an OrderedDict in insertion order after sorting.

Example Input:
{'c': 3, 'a': 1, 'b': 2}

Example Output:
OrderedDict([('a', 1), ('b', 2), ('c', 3)])
'''

'''
7. Find and Replace in an OrderedDict

Task: Create an OrderedDict and replace the value of a specific key. Write a function that updates the value without changing the order of items.

Example Input:
OrderedDict([('a', 1), ('b', 2), ('c', 3)])
Update key: 'b' to 5

Example Output:
OrderedDict([('a', 1), ('b', 5), ('c', 3)])
'''

'''
8. Difference Between Two OrderedDicts

Task: Write a program to compare two OrderedDicts and find the differences in keys and values while respecting the order.

Example Input:
dict1 = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
dict2 = OrderedDict([('a', 1), ('b', 4), ('d', 5)])

Example Output:
Keys in dict1 but not in dict2: ['c']
Keys in dict2 but not in dict1: ['d']
Different values: {'b': (2, 4)}
'''
