'''
0. Create an iterator that counts numbers starting from 1 and continues until a specified limit
'''
class Counter:
    def __init__(self, max_count):
        self.max_count = max_count
        self.count = 1 # current count, initially set to 1
    def __iter__(self):  # this itself is the iterator
        return self
    def __next__(self):
        if self.count > self.max_count:
            raise StopIteration
        else:
            current = self.count
            self.count += 1
            return current

# counter = Counter(5)
# for num in counter:
#     print(num)

'''
Create a custom iterator class EvenNumbers that takes a max_number as input and iterates through all even numbers form 2 to max_number
'''

class EvenNumbers:
    def __init__(self, max_number):
        self.max_number = max_number
        self.count = 2
    def __iter__(self):
        return self
    def __next__(self):
        if self.count > self.max_number:
            raise StopIteration
        else:
            current = self.count
            self.count += 2
            return current

# loop = EvenNumbers(14)
# for number in loop:
#     print(number)


'''
1. Custom Iterator

	•	Task: Create a custom iterator class Reverse that takes a string as input and iterates through the string in reverse order.
	•	Example Input: "Hello"
	•	Example Output: 'o', 'l', 'l', 'e', 'H'
'''

class Reverse:
    def __init__(self, string):
        self.string = string
        self.max = len(self.string) - 1
        self.count = self.max
    def __iter__(self):
        return self
    def __next__(self):
        if self.count < 0:
            raise StopIteration
        else:
            current = self.string[self.count]
            self.count -= 1
            return current


# reversed_string_letters = Reverse("Hello")
# for letter in reversed_string_letters:
#     print(letter)

'''
2. Even Numbers Generator

	•	Task: Write a generator function even_numbers that yields even numbers starting from 0, and stops once it reaches a specified limit.
	•	Example Input: even_numbers(10)
	•	Example Output: 0, 2, 4, 6, 8
'''


'''
3. Fibonacci Sequence Generator

	•	Task: Create a generator fibonacci that yields the Fibonacci sequence up to a given number of terms.
	•	Example Input: fibonacci(5)
	•	Example Output: 0, 1, 1, 2, 3
'''

'''
4. Prime Number Generator

	•	Task: Write a generator prime_numbers that yields prime numbers up to a given limit.
	•	Example Input: prime_numbers(20)
	•	Example Output: 2, 3, 5, 7, 11, 13, 17, 19
'''

'''
5. Custom Iterable Class

	•	Task: Create a custom iterable class RangeSquares that generates the squares of numbers in a specified range.
	•	Example Input: RangeSquares(1, 5)
	•	Example Output: 1, 4, 9, 16
'''

'''
6. Infinite Generator

	•	Task: Write an infinite generator count_up_from that yields numbers starting from a given value and continues indefinitely.
	•	Example Input: count_up_from(5)
	•	Example Output: 5, 6, 7, 8, 9, ... (This will run indefinitely, so use itertools.islice() to limit the output.)
'''

'''
7. Sum of Squares

	•	Task: Create a generator sum_of_squares that yields the sum of squares of numbers starting from 1 and stops when the sum exceeds a given limit.
	•	Example Input: sum_of_squares(50)
	•	Example Output: 1, 5, 14, 30, 55 (Sum of squares: 1, 1+4=5, 1+4+9=14, etc.)
'''

'''
8. Custom Iterator to Filter Odd Numbers

	•	Task: Create an iterator OddFilter that iterates through a list and returns only the odd numbers.
	•	Example Input: [1, 2, 3, 4, 5]
	•	Example Output: 1, 3, 5
'''

'''
9. Exponentiation Generator

	•	Task: Write a generator powers_of_two that yields successive powers of 2 starting from 1 up to a given exponent.
	•	Example Input: powers_of_two(5)
	•	Example Output: 1, 2, 4, 8, 16
'''

'''
10. Countdown Generator

	•	Task: Write a generator countdown that generates a countdown sequence starting from a given number down to 0.
	•	Example Input: countdown(5)
	•	Example Output: 5, 4, 3, 2, 1, 0
'''

