from collections import OrderedDict

d = OrderedDict([('apple', 5), ('orange', 6)])
print(d)

d['kiwi'] = 7
print(d)

o = OrderedDict()  # we can initialise an empty ordered dictionary

o['bowls'] = 7     # and then populate it
o['plates'] = 20
print(o)
print(o.items())

some = OrderedDict([('plates', 6), ('spoons', 18), ('forks', 2)])
print(some)
print(some.items())
print(some.keys())
print(some.values())
print(OrderedDict(reversed(some.items())))
