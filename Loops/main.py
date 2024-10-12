
"""
Make a list of game scores. Using list functions write code to output information of the scores in the following format:
    Number of scores: 10
    Highest score: 200
    Lowest score: 3
Extension: Output all of the scores in descending order
"""
score_list = [22, 7, 3, 9, 25, 7, 8, 6, 3, 200]
print(f"Number of scores: {len(score_list)}")
print(f"Higest score: {max(score_list)}")
print(f"Lowest score: {min(score_list)}")

""""
Whenever I'm shopping and I buy some bread I always forget to buy butter.
Create a list and if 'bread' is in the list, add 'butter' to the shopping list.
Try running the program with and without bread in the list to check that your program works.
Remember the in operator checks if an item is in a list and the .append() method adds an item to a list.
"""

shopping_list_1 = ['eggs', 'bread', 'milk', 'chilli flakes']
shopping_list_2 = ['eggs', 'milk', 'chilli flakes']

if 'bread' in shopping_list_1:
    shopping_list_1.append('butter')

if 'bread' in shopping_list_2:
    shopping_list_2.append('butter')

print(f"shopping_list_1: {shopping_list_1}")
print(f"shopping_list_2: {shopping_list_2}")      
      
'''
Print the values of name, post_code and street_number from the dictionary
'''


place = {'name': 'The Anchor', 'post_code': 'E14 6HY', 'street_number': '54','location': {'longitude': 127, 'latitude': 63}}
print(place['name'])
print(place['post_code'])
print(place['street_number'])

"""
Using a for loop, output the values name, colour and price of each dictionary in the list
"""
fruits = [

    {'name': 'apple', 'colour': 'red', 'price': 0.12},

    {'name': 'banana', 'colour': 'yellow', 'price': 0.2},

    {'name': 'pear', 'colour': 'green', 'price': 0.19},

]

for i in range(len(fruits)):
    print(fruits[i]['name'])
    print(fruits[i]['colour'])
    print(fruits[i]['price'])

names=[]
colours = []
prices = []

for a in range()

