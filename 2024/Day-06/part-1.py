with open("input.txt") as f:  # noqa: PTH123, INP001, D100
    lines = [list(line.strip()) for line in f]
    lines_length = len(lines)
    position_markers = ["^", "v", ">", "<"]
    marker_movements = {
        "^": (-1, 0),
        "v": (1, 0),
        ">": (0, 1),
        "<": (0, -1),
    }
    next_marker = {"^": ">", ">": "v", "v": "<", "<": "^"}

    position_found = False
    for i in range(lines_length):
        for j in range(lines_length):
            if lines[i][j] in position_markers:
                position_marker = lines[i][j]
                position = (i, j)
                position_found = True
                break

        if position_found:
            break

    visited = set()
    while True:
        visited.add(position)

        dx, dy = marker_movements[position_marker]
        i, j = position[0] + dx, position[1] + dy

        if not (0 <= i < lines_length and 0 <= j < lines_length):
            break

        if lines[i][j] == "#":
            position_marker = next_marker[position_marker]
            i, j = position

        position = (i, j)

    print(len(visited))  # noqa: T201

"""
4647
         5429 function calls in 0.004 seconds

   Ordered by: cumulative time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.004    0.004 {built-in method builtins.exec}
        1    0.003    0.003    0.004    0.004 part-1.py:1(<module>)
     5279    0.000    0.000    0.000    0.000 {method 'add' of 'set' objects}
        1    0.000    0.000    0.000    0.000 {built-in method _io.open}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.print}
      130    0.000    0.000    0.000    0.000 {method 'strip' of 'str' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        5    0.000    0.000    0.000    0.000 <frozen codecs>:319(decode)
        1    0.000    0.000    0.000    0.000 {method '__exit__' of '_io._IOBase' objects}
        5    0.000    0.000    0.000    0.000 {built-in method _codecs.utf_8_decode}
        1    0.000    0.000    0.000    0.000 <frozen codecs>:309(__init__)
        2    0.000    0.000    0.000    0.000 {built-in method builtins.len}
        1    0.000    0.000    0.000    0.000 <frozen codecs>:260(__init__)
"""
