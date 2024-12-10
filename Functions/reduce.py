'''
Given a list of letters, use the reduce() higher-order function with a lambda 
function to combine the letters into a single word:
letters = ['r', 'e', 'd', 'u', 'c', 'e']
'''

letters = ['r', 'e', 'd', 'u', 'c', 'e']

from functools import reduce

word = reduce(lambda x, y: x+y, letters)
print(word)