import itertools

result = itertools.count(start=0, step=2) # takes two optional arguments and returns an iterator
print(result.__next__())
print(result.__next__())
print(result.__next__())
print(result.__next__())

example = itertools.cycle('12345') # takes in something you can iterate over and goes over it indefinitely

result_again = itertools.repeat(object='CodeFirstGirls', times=2)  # repeats an element a specified number of times. takes an optional times parameter that can be used as a termination condition
for word in result_again:
    print(word)
