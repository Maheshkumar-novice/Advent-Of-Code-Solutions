with open("input.txt") as f:
    grid_data = [list(line.strip()) for line in f]

directions = [
    (-1, -1),
    (-1, 1),  # Top row
    (1, -1),
    (1, 1),  # Bottom row
]
allowed_val = ["M", "S"]
values = ["1", "2", "3", "4"]
count = 0
grid_length = len(grid_data)

for row in range(grid_length):
    for col in range(grid_length):
        if grid_data[row][col] != "A":
            continue

        updates = 0
        for idx, (dx, dy) in enumerate(directions):
            new_row, new_col = row + dx, col + dy
            if 0 <= new_row < grid_length and 0 <= new_col < grid_length and grid_data[new_row][new_col] in allowed_val:
                values[idx] = grid_data[new_row][new_col]
                updates += 1

        if updates == 4 and values[0] != values[3] and values[1] != values[2]:
            count += 1
print(count)


"""
# python 3.13
 python3 -m cProfile part-2.py
2046
         159 function calls in 0.030 seconds

   Ordered by: cumulative time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.030    0.030 {built-in method builtins.exec}
        1    0.030    0.030    0.030    0.030 part-2.py:1(<module>)
      140    0.000    0.000    0.000    0.000 {method 'strip' of 'str' objects}
        1    0.000    0.000    0.000    0.000 {built-in method _io.open}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.print}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        5    0.000    0.000    0.000    0.000 <frozen codecs>:322(decode)
        1    0.000    0.000    0.000    0.000 {method '__exit__' of '_io._IOBase' objects}
        5    0.000    0.000    0.000    0.000 {built-in method _codecs.utf_8_decode}
        1    0.000    0.000    0.000    0.000 <frozen codecs>:312(__init__)
        1    0.000    0.000    0.000    0.000 <frozen codecs>:263(__init__)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
"""
