from itertools import cycle

colors = cycle(["red", "green", "blue"])

for i in range(5):
    print(next(colors))