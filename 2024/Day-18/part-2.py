import re
from collections import deque
from functools import cache

with open("input.txt") as f:
    grid_length = 71

    grid = [["." for _ in range(grid_length)] for _ in range(grid_length)]
    directions = {"n": (-1, 0), "s": (1, 0), "e": (0, 1), "w": (0, -1)}
    memory_bytes = [(int(x), int(y)) for y, x in re.findall(r"(?:(\d+),(\d+))", f.read())]

    @cache
    def _next_directions(x: int, y: int):  # noqa: ANN202
        next_directions = []
        for direction in list(directions.keys()):
            dx, dy = directions[direction]
            nx, ny = x + dx, y + dy
            if 0 <= nx < grid_length and 0 <= ny < grid_length:
                next_directions.append((nx, ny))
        return next_directions

    for x, y in memory_bytes[:1024]:
        grid[x][y] = "#"

    for dx, dy in memory_bytes[1024:]:
        grid[dx][dy] = "#"

        queue = deque([(0, 0, 0)])
        min_score = float("inf")
        visited = set()
        while queue:
            x, y, score = queue.popleft()
            if (x, y) in visited:
                continue
            visited.add((x, y))

            for nx, ny in _next_directions(x, y):
                if grid[nx][ny] == "#":
                    continue
                elif (nx, ny) == (grid_length - 1, grid_length - 1):
                    min_score = min(score + 1, min_score)
                else:
                    queue.append((nx, ny, score + 1))

        if min_score == float("inf"):
            print(dy, dx)
            # print(_next_directions.cache_info())
            break
