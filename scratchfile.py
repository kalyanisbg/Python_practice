from collections import OrderedDict

# Example OrderedDict
ordered_dict = OrderedDict([('apple', 4), ('banana', 2), ('cherry', 3), ('date', 1)])

# Sort by values (ascending order)
sorted_by_values = OrderedDict(sorted(ordered_dict.items(), key=lambda item: item[1]))

print(sorted_by_values)  # Output: OrderedDict([('date', 1), ('banana', 2), ('cherry', 3), ('apple', 4)])