from collections import Counter

a_list = [1, 2, 2, 2, 3, 3, 3, 4, 5, 6, 6, 7]
a_string = 'CodeFirstGirls'
a_dict = {
    'a': 3,
    'b': 6,
    'c': 8,
    'd': 3,
    'e': 9
}

c_list = Counter(a_list)
print(c_list)
print(Counter(a_string))
print(Counter(a_dict))