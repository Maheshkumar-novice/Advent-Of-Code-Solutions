from functools import reduce

with open('input.txt', 'r') as f:
    def get_fuel(x): return 0 if x <= 0 else x + get_fuel(int(x) // 3 - 2)

    print(reduce(lambda x, y: x + get_fuel(int(y) // 3 - 2), f, 0))
