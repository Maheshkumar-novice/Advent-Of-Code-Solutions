from collections import deque
from functools import cache
from time import monotonic

st = monotonic()
with open("input.txt") as f:
    grid = [list(line.strip()) for line in f]
    directions = {"n": (-1, 0), "s": (1, 0), "e": (0, 1), "w": (0, -1)}
    possible_directions_from = {"n": ["e", "w"], "s": ["e", "w"], "e": ["n", "s"], "w": ["n", "s"]}
    vertice_scores = {}
    grid_length = len(grid)
    sx, sy = next((i, j) for i in range(grid_length) for j in range(grid_length) if grid[i][j] == "S")

    @cache
    def _next_directions(x: int, y: int, current_direction: str):  # noqa: ANN202
        next_directions = []
        for direction in (current_direction, *possible_directions_from[current_direction]):
            dx, dy = directions[direction]
            nx, ny = x + dx, y + dy
            if 0 <= nx < grid_length and 0 <= ny < grid_length and grid[nx][ny] != "#":
                next_directions.append((direction, nx, ny))
        return next_directions

    queue = deque([(sx, sy, 0, "e")])
    visited = set()
    min_score = float("inf")
    while queue:
        x, y, score, direction = queue.popleft()
        if (x, y, direction) in vertice_scores and score > vertice_scores[(x, y, direction)]:
            continue
        vertice_scores[(x, y, direction)] = score

        for new_direction, nx, ny in _next_directions(x, y, direction):
            if grid[nx][ny] == "E":
                min_score = min(score + 1, min_score)
            elif new_direction == direction:
                queue.append((nx, ny, score + 1, new_direction))
            else:
                queue.append((x, y, score + 1000, new_direction))

print(min_score)
# print(monotonic() - st)

"""
0.28190441703191027
"""
