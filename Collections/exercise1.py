"""
Use a defaultdict to store a count for each character that appears in a given string. 

Print the most common character in this dictionary.
"""

from collections import defaultdict

count_dict = defaultdict(int)

string = "CodeFirstGirls".lower()
for i in string:
    count_dict[i] += 1

print(count_dict)

highest = 0
most_common_chars = []
for key, value in count_dict.items():
    if value > highest:
        highest = value
        most_common = key
        most_common_chars.append(key)

print(most_common_chars)





