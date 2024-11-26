numbers = [3, 8, 19, 0, 2, 34, 2, -1]
print(iter(numbers))  # generates an iterator
print(next(iter(numbers))) 
print(next(iter(numbers)))
print(next(iter(numbers))) # generates a fresh iterator everytime you call, hence starts fresh
print(next(iter(numbers)))

print("Trying something different")
iterator = iter(numbers)
print(next(iterator)) # calls the same 'iterator' variable and hence iterates through rather than giving the same number over and over again
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator)) # the next step breaks it and throws a StopIteration exception


# Alternative - traversing - same as next but different usage
nums_iter2 = iter({1, 2, 3, 4, 5})
print(nums_iter2.__next__())
print(nums_iter2.__next__())
print(nums_iter2.__next__())
print(nums_iter2.__next__())
#print(nums_iter2.__next__())  this step breaks it

# list out available methods

print(dir(nums_iter2))  # use pretty print to make the result look more readable