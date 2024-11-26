'''
make a function that counts down from whatever number
we supply and then prints 'blast off'
'''

def countdown(n):
    for i in range(n):
        print(n - i)
    
    print('blast off!')

def countdown_with_recursion(n):  # keep printing the number until its zero
    if n == 0:  # base case - when do you want the function to stop?
        print('blast off!')
    else:
        print(n)
        countdown_with_recursion(n-1)


'''
function to return the factorial of a number
'''
def factorial(n):
    result = 1
    for i in range(1, n+1):
        print(f"result: {result}")
        result *= i
    return result

def factorial_with_recursion(n):
    if n == 1:
        return 1
    else:
        return n * factorial_with_recursion(n - 1)

    # 3 * 2 * 1

# print(factorial_with_recursion(4))

'''
write a fibonacci sequence
1, 1, 2, 3, 5, 8, 13, 21, 34 ....
'''

def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [1]
    elif n == 2:
        return [1, 1]
    else:
        sequence = [1, 1]
        for number in range(2, n):
            sequence.append(sequence[-1] + sequence[-2])
            return sequence


def fibonacci_recursive(n):
    if n <= 0:
        return []
    elif n == 1:
        return [1]
    elif n == 2:
        return [1, 1]
    else:
        sequence = fibonacci_recursive(n-1)
        sequence.append(sequence[-1] + sequence[-2])
        return sequence