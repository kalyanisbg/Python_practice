from collections import OrderedDict

d = OrderedDict([('apple', 5), ('orange', 6)])
print(d)

d['kiwi'] = 7
print(d)

o = OrderedDict()  # we can initialise an empty ordered dictionary

o['bowls'] = 7     # and then populate it
o['plates'] = 20
print(o)