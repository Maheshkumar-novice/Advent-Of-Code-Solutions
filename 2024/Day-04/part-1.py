with open("input.txt") as f:
    grid_data = [list(line.strip()) for line in f]

directions = [
    (-1, -1),
    (-1, 0),
    (-1, 1),  # Top row
    (0, -1),
    (0, 1),  # Same row (left and right)
    (1, -1),
    (1, 0),
    (1, 1),  # Bottom row
]
count = 0
grid_length = len(grid_data)
xmas = "XMAS"
for dx, dy in directions:
    for row in range(grid_length):
        for col in range(grid_length):
            text = grid_data[row][col]
            if text != "X":
                continue
            temp_row, temp_col = row, col
            for _ in range(3):
                new_row, new_col = temp_row + dx, temp_col + dy
                if 0 <= new_row < grid_length and 0 <= new_col < grid_length:
                    text += grid_data[new_row][new_col]
                temp_row, temp_col = new_row, new_col
            if text == xmas:
                count += 1
print(count)


"""
# python 3.13
 python3 -m cProfile part-1.py
2718
         159 function calls in 0.075 seconds

   Ordered by: cumulative time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.075    0.075 {built-in method builtins.exec}
        1    0.075    0.075    0.075    0.075 part-1.py:1(<module>)
        1    0.000    0.000    0.000    0.000 {built-in method _io.open}
      140    0.000    0.000    0.000    0.000 {method 'strip' of 'str' objects}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.print}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        5    0.000    0.000    0.000    0.000 <frozen codecs>:322(decode)
        1    0.000    0.000    0.000    0.000 {method '__exit__' of '_io._IOBase' objects}
        5    0.000    0.000    0.000    0.000 {built-in method _codecs.utf_8_decode}
        1    0.000    0.000    0.000    0.000 <frozen codecs>:312(__init__)
        1    0.000    0.000    0.000    0.000 <frozen codecs>:263(__init__)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
"""
