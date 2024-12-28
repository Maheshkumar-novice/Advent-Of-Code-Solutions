import re
from collections import deque

with open("input.txt") as f:
    grid_length = 71
    grid = [["." for j in range(grid_length)] for i in range(grid_length)]
    directions = {"n": (-1, 0), "s": (1, 0), "e": (0, 1), "w": (0, -1)}
    memory_bytes = [(int(x), int(y)) for y, x in re.findall(r"(?:(\d+),(\d+))", f.read())]

    def _next_directions(x: int, y: int):  # noqa: ANN202
        next_directions = []
        for dx, dy in directions.values():
            nx, ny = x + dx, y + dy
            if 0 <= nx < grid_length and 0 <= ny < grid_length and grid[nx][ny] != "#":
                next_directions.append((nx, ny))
        return next_directions

    for x, y in memory_bytes[:1024]:
        grid[x][y] = "#"

    queue = deque([(0, 0, 0)])
    min_score = float("inf")
    visited = set()
    while queue:
        x, y, score = queue.popleft()
        grid[x][y] = "O"
        if (x, y) in visited:
            continue
        visited.add((x, y))

        for nx, ny in _next_directions(x, y):
            if (nx, ny) == (grid_length - 1, grid_length - 1):
                min_score = min(score + 1, min_score)
            else:
                queue.append((nx, ny, score + 1))
    print(min_score)
