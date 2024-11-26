'''
1. Word Frequency Counter

Write a function that takes a string and returns the frequency of each word in the string.
Example Input:
"apple banana apple orange banana apple"
Output:
{'apple': 3, 'banana': 2, 'orange': 1}
'''
from collections import Counter


def word_freq(string):
    words = string.split()
    return Counter(words)

# print(word_freq("apple banana apple orange banana apple"))

'''
2. Most Common Element

Given a list of numbers, find the most common number and its frequency.
Example Input:
[1, 3, 3, 2, 1, 1, 4, 3]
Output:
Most common: 3, Frequency: 3
'''

def most_common_number(numbers):
    frequency = max(Counter(numbers).values())
    keys = [key for key, value in Counter(numbers).items() if value == frequency]
    return f"Most common: {keys}, Frequency: {frequency}"

# print(most_common_number([1, 3, 3, 2, 1, 1, 4, 3]))

'''
3. Character Frequency in a String

Write a function that counts the frequency of each character in a string, ignoring case and spaces.
Example Input:
"Hello World"
Output:
{'h': 1, 'e': 1, 'l': 3, 'o': 2, 'w': 1, 'r': 1, 'd': 1}
'''

def char_freq(string):
    string = string.lower()
    string = string.replace(' ', '')
    return Counter(string)

# print(char_freq("Hello World"))

'''
4. Top N Common Elements

Given a list of items, find the top n most common elements.
Example Input:
List: ['a', 'b', 'a', 'c', 'b', 'a', 'b', 'c'], n = 2
Output:
[('a', 3), ('b', 3)]
'''

'''
5. Check Anagrams

Write a function that checks if two strings are anagrams (ignoring spaces and case). Use Counter to compare their character frequencies.
Example Input:
"Listen" and "Silent"
Output:
True
'''

'''
6. Element Frequency in a Matrix

Count how often each number appears in a 2D matrix.
Example Input:
[[1, 2, 3], [1, 1, 2], [3, 4, 4]]
Output:
{1: 3, 2: 2, 3: 2, 4: 2}
'''

'''
7. Remove Elements with Frequency Below N

Write a function that removes all elements from a list that appear fewer than n times.
Example Input:
List: [1, 2, 2, 3, 3, 3], n = 2
Output:
[2, 2, 3, 3, 3]
'''

'''
8. Merge Counters

Given two dictionaries representing word counts, merge them into a single Counter and display the combined frequencies.
Example Input:
{'apple': 2, 'banana': 1} and {'banana': 2, 'orange': 1}
Output:
{'apple': 2, 'banana': 3, 'orange': 1}
'''

'''
9. Frequency of Even and Odd Numbers

Count how many even and odd numbers appear in a list.
Example Input:
[1, 2, 3, 4, 5, 6, 7, 8]
Output:
{'even': 4, 'odd': 4}
'''

'''
10. Count Substrings in a String

Write a function that counts the occurrences of all substrings of a given length in a string.
Example Input:
String: "banana", Substring Length: 2
Output:
{'ba': 1, 'an': 2, 'na': 2}
'''