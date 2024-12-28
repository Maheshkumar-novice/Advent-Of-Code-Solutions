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

    visited, original_position, original_position_marker = set(), position, position_marker
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

    position, position_marker, count = original_position, original_position_marker, 0
    for x, y in visited:
        if (x, y) == position:
            continue
        if lines[x][y] == "#":
            continue

        lines[x][y] = "#"
        original_position = position
        old_position_marker = position_marker

        visited_obstacles_in_direction = set()
        while True:
            dx, dy = marker_movements[position_marker]
            i, j = position[0] + dx, position[1] + dy

            if not (0 <= i < lines_length and 0 <= j < lines_length):
                break

            if lines[i][j] == "#":
                obstacle_ident = (i, j, position_marker)
                if obstacle_ident not in visited_obstacles_in_direction:
                    visited_obstacles_in_direction.add(obstacle_ident)
                else:
                    count += 1
                    break
                position_marker = next_marker[position_marker]
                i, j = position
            position = (i, j)

        position = original_position
        position_marker = old_position_marker
        lines[x][y] = "."

    print(count)  # noqa: T201

"""
1723
         424072 function calls in 3.672 seconds

   Ordered by: cumulative time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    3.672    3.672 {built-in method builtins.exec}
        1    3.633    3.633    3.672    3.672 part-2.py:1(<module>)
   423923    0.039    0.000    0.039    0.000 {method 'add' of 'set' objects}
        1    0.000    0.000    0.000    0.000 {built-in method _io.open}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.print}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        1    0.000    0.000    0.000    0.000 {method '__exit__' of '_io._IOBase' objects}
      130    0.000    0.000    0.000    0.000 {method 'strip' of 'str' objects}
        5    0.000    0.000    0.000    0.000 <frozen codecs>:319(decode)
        5    0.000    0.000    0.000    0.000 {built-in method _codecs.utf_8_decode}
        1    0.000    0.000    0.000    0.000 <frozen codecs>:309(__init__)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
        1    0.000    0.000    0.000    0.000 <frozen codecs>:260(__init__)
"""
