import itertools

"""
Exercise 1: Repeat a Number
Task: Use itertools.repeat to repeat the number 5 for 8 times and print the result.

Expected Output:
5
5
5
5
5
5
5
5
"""

repeat_tool = itertools.repeat(5, times=8)
for five in repeat_tool:
    print(five)

"""
Exercise 2: Repeat a String
Task: Use itertools.repeat to repeat the string "Hello" 4 times and print each repetition on a new line.

Expected Output:
Hello
Hello
Hello
Hello
"""

repeat_tool2 = itertools.repeat("Hello", times=4)
for item in repeat_tool2:
    print(item)