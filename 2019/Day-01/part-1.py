from functools import reduce

with open('input.txt', 'r') as f:
    print(reduce(lambda x, y: x + int(y) // 3 - 2, f, 0))
