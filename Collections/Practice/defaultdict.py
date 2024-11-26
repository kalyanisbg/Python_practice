from collections import defaultdict

'''
1. Counting Word Frequency

	•	Task: Given a list of words, use a defaultdict to count the frequency of each word.
	•	Input: ["apple", "banana", "apple", "orange", "banana", "apple"]
	•	Output: {'apple': 3, 'banana': 2, 'orange': 1}
'''

def word_freq_dict(words):
    result = defaultdict(int)
    for word in words:
        result[word] += 1
    return dict(result)

# print(word_freq_dict(["apple", "banana", "apple", "orange", "banana", "apple"]))

'''
2. Grouping Words by First Letter

	•	Task: Given a list of words, group them by their first letter using a defaultdict. The key will be the first letter, and the value will be a list of words starting with that letter.
	•	Input: ["apple", "banana", "apricot", "blueberry", "orange"]
	•	Output: {'a': ['apple', 'apricot'], 'b': ['banana', 'blueberry'], 'o': ['orange']}
'''

def words_by_first_letter(words):
    result = defaultdict(list)
    for word in words:
        result[word[0]].append(word)
    return dict(result)

# print(words_by_first_letter(["apple", "banana", "apricot", "blueberry", "orange"]))

'''
3. Storing Grades

	•	Task: You are given a list of student names and their grades. Use a defaultdict to store the grades for each student. Each student can have multiple grades, so the value should be a list of grades.
	•	Input: [("Alice", 85), ("Bob", 90), ("Alice", 92), ("Bob", 88), ("Charlie", 78)]
	•	Output: {'Alice': [85, 92], 'Bob': [90, 88], 'Charlie': [78]}
'''

def student_grades(students_and_grades):
    student_grades = defaultdict(list)
    for element in students_and_grades:
        student_grades[element[0]].append(element[1])
    return dict(student_grades)

print(student_grades([("Alice", 85), ("Bob", 90), ("Alice", 92), ("Bob", 88), ("Charlie", 78)]))

'''
4. Categorizing Numbers by Parity

	•	Task: Given a list of integers, categorize them into “even” and “odd” using a defaultdict. The key should be “even” or “odd”, and the value should be a list of numbers in that category.
	•	Input: [1, 2, 3, 4, 5, 6]
	•	Output: {'odd': [1, 3, 5], 'even': [2, 4, 6]}
'''

'''
5. Creating a Frequency Table

	•	Task: Given a list of characters (some repeated), create a frequency table using a defaultdict where each key is a character, and the value is its frequency.
	•	Input: ['a', 'b', 'a', 'c', 'a', 'b', 'c', 'd']
	•	Output: {'a': 3, 'b': 2, 'c': 2, 'd': 1}
'''

'''
6. Mapping Items to Categories

	•	Task: Given a list of tuples where each tuple contains an item and its category, use a defaultdict to categorize the items. Each key should be a category, and the value should be a list of items in that category.
	•	Input: [("apple", "fruit"), ("carrot", "vegetable"), ("banana", "fruit"), ("broccoli", "vegetable")]
	•	Output: {'fruit': ['apple', 'banana'], 'vegetable': ['carrot', 'broccoli']}
'''

'''
7. Flattening a List of Lists

	•	Task: Given a list of lists, use a defaultdict to flatten the list. Each key will be the index of the sublist, and the value will be a list of items at that index across all sublists.
	•	Input: [[1, 2], [3, 4], [5, 6]]
	•	Output: {0: [1, 3, 5], 1: [2, 4, 6]}
'''

'''
8. Default Dictionary with Integer Values

	•	Task: Use a defaultdict(int) to calculate the cumulative sum of integers from a list, such that the dictionary stores the cumulative sum for each index.
	•	Input: [5, 3, 6, 2]
	•	Output: {0: 5, 1: 8, 2: 14, 3: 16}
'''

'''
9. Creating a Dictionary of Sets

	•	Task: Given a list of tuples where each tuple represents a relationship between two items, use a defaultdict(set) to store a set of related items. The keys will be items, and the values will be the related items.
	•	Input: [("Alice", "Bob"), ("Alice", "Charlie"), ("Bob", "Charlie"), ("Charlie", "Dave")]
	•	Output: {'Alice': {'Bob', 'Charlie'}, 'Bob': {'Alice', 'Charlie'}, 'Charlie': {'Alice', 'Bob', 'Dave'}, 'Dave': {'Charlie'}}
'''

'''
10. Finding Common Elements Between Lists

	•	Task: Given a list of lists, use a defaultdict(int) to find the common elements between all lists. The key will be the element, and the value will be how many times that element appears in all the lists.
	•	Input: [[1, 2, 3], [2, 3, 4], [3, 5, 6]]
	•	Output: {3: 3, 2: 2}
'''

'''
Bonus Challenge: Building a Dictionary of Lists (with Multiple Values)

	•	Task: Given a list of strings, use a defaultdict(list) to store each character of the string as a key and the indices where the character occurs as the value.
	•	Input: ["apple", "banana", "grape"]
	•	Output: {'a': [0, 1, 4, 6], 'p': [1, 2], 'l': [3], 'e': [4], 'b': [0], 'n': [1, 2], 'g': [0], 'r': [2]}
'''

