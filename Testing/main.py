"""
Task
Given an integer x perform the following conditional actions:
If x is odd, return 'Red'
If x is even and in the inclusive range of 2 to 5, return 'Blue'
If x is even and in the inclusive range of 6 to 20, return 'Red'
If x is even and greater than 20, return 'Blue'
Constraint notes:
an input integer is always withing the range 1 to 100 inclusive

"""

def red_or_blue(num):
    if num % 2 != 0:  # If x is odd
        return 'Red'
    elif 2 <= num <= 5:  # If x is even and between 2 and 5 inclusive
        return 'Blue'
    elif 6 <= num <= 20:  # If x is even and between 6 and 20 inclusive
        return 'Red'
    else:  # If x is even and greater than 20
        return 'Blue'
