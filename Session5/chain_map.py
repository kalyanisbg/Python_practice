from collections import ChainMap

dict1 = {
    'apple': 1,
    'banana': 2,
}

dict2 = {
    'coconut': 1,
    'date': 1,
    'apple': 3
}

combined_dict = ChainMap(dict1, dict2)
reversed_dict = ChainMap(dict2, dict1)
print(combined_dict)  # gives two separate dictionaries in a list
print(reversed_dict)

for key, value in combined_dict.items():
    print(key, value)   # will say apple is  1

for key, value in reversed_dict.items():
    print(key, value)   # will say apple is 3


print(combined_dict['apple'])
print(reversed_dict['apple'])
