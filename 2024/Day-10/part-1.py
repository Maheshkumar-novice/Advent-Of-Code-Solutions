from collections import deque  # noqa: INP001, D100
from collections.abc import Generator
from time import monotonic
from typing import Any

s = monotonic()

with open("input.txt") as f:  # noqa: PTH123
    grid = [list(map(int, line.strip())) for line in f]
    grid_length = len(grid)

    trailheads = [(i, j) for i in range(grid_length) for j in range(grid_length) if grid[i][j] == 0]

    possible_directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]

    def _get_neighbours(x: int, y: int) -> Generator[tuple[int, int], Any, None]:
        for dx, dy in possible_directions:
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x < grid_length and 0 <= new_y < grid_length and grid[x][y] + 1 == grid[new_x][new_y]:
                yield (new_x, new_y)

    result = 0
    for trailhead in trailheads:
        q = deque([trailhead])
        nines = set()

        while q:
            x, y = q.popleft()

            for new_x, new_y in _get_neighbours(x, y):
                if grid[new_x][new_y] == 9:
                    nines.add((new_x, new_y))
                    continue
                q.append((new_x, new_y))

        result += len(nines)

    print(result)  # noqa: T201

"""
0.007643263001227751
"""
