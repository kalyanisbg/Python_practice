# 1. Functions are objects

def add_five(num):
    print(num + 5)

add_five(9)  # prints 14
add_five   # doesn't print anything but also doesn't give an error

print(add_five)
'''
you get the memory address of add_five
because add_five is an object
'''

# 2. Functions within functions

