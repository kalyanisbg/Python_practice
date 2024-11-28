import itertools

"""
Exercise 1: Repeating Colors
Task: Use itertools.cycle to create an infinite cycle of colors: ["Red", "Green", "Blue"].
Print the first 10 colors in the sequence.

Expected Output:
Red
Green
Blue
Red
Green
Blue
Red
Green
Blue
Red
"""

# create an iterator
# limit the iterator to 10 colors
# print the colors

# colors = ["Red", "Green", "Blue"]
# iterator0 = itertools.cycle(colors)
# count = 0
# for color in iterator0:
#     if count < 10:
#         count += 1
#         print(color)
#     else:
#         break

"""
Exercise 2: Cycling Through Days of the Week
Task: Use itertools.cycle to cycle through the days of the week: ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"].
Stop cycling after printing the first 15 days.

Expected Output:
Monday
Tuesday
Wednesday
...
(Similar for 15 days in sequence)
"""

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
iterator1 = itertools.cycle(days)
count = 0
for day in iterator1:
    if count < 15:
        count += 1
        print(day)
    else:
        break