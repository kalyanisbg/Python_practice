'''
1. Reverse Integer
Given an integer, return the integer with reversed digits.
Note: The integer could be either positive or negative
123 => 321
-456 => -654
'''

def reversed_integer(integer):
    # convert into string
    string = str(integer)
    # if first element is - keep it as such
    if string[0] == '-':
        return int('-' + string[:0:-1])
    else:
        return int(string[::-1])
    return int(new_str)
    # else last index becomes first

print(reversed_integer(123))
print(reversed_integer(-456))