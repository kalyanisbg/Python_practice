from collections import deque

d = deque('CodeFirstGirls')
print(d)

d.append('!')
d.appendleft('ThisIs')   # adds to the start of the iterable - ThisIs is treated as a single unit
print(d)

d.pop()
d.popleft()
print(d)

d.extend('123')   # 123 is treated as separate units
d.extendleft('456')
print(d)

d.rotate(3)
print(d)
d.rotate(-2)
print(d)

d.clear()   # clears everything in the list d
print(d)