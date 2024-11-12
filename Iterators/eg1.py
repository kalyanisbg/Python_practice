num = [2, 5, 1, 9, 6]

nums_iter = iter(num)
print(nums_iter)

print(next(nums_iter))
print(next(nums_iter))
print(next(nums_iter))


# Alternative - traversing
nums_iter2 = iter({1, 2, 3, 4, 5})
print(next(nums_iter2))

# list out available methods

print(dir(nums_iter))  # use pretty print to make the result look more readable