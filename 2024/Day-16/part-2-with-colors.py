import os
from collections import defaultdict, deque
from functools import cache
from time import monotonic, sleep

st = monotonic()
with open("sample.txt") as f:
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

    queue = deque([(sx, sy, 0, "e", [])])
    visited = set()
    min_score = float("inf")
    path_len = defaultdict(set)
    while queue:
        x, y, score, direction, path = queue.popleft()
        path.append((x, y, direction, score))
        grid[x][y] = f"\033[31m{'O'}\033[0m"
        if (x, y, direction) in vertice_scores and score > vertice_scores[(x, y, direction)]:
            continue
        vertice_scores[(x, y, direction)] = score

        for new_direction, nx, ny in _next_directions(x, y, direction):
            if grid[nx][ny] == "E":
                ex, ey = nx, ny
                min_score = min(score + 1, min_score)
                for fx, fy, _, _ in path:
                    path_len[score + 1].add((fx, fy))
            elif new_direction == direction:
                queue.append((nx, ny, score + 1, new_direction, path.copy()))
            else:
                queue.append((x, y, score + 1000, new_direction, path.copy()))
        os.system("clear")  # noqa: S605, S607
        print("\n".join(["".join(line) for line in grid]) + f"\nScore: {score + 1}")
        sleep(0.1)

print(monotonic() - st)
print(path)

for i in range(grid_length):
    for j in range(grid_length):
        if grid[i][j] == "#":
            grid[i][j] = f"\033[34m{'#'}\033[0m"

for dx, dy in path_len[min_score]:
    grid[dx][dy] = f"\033[1;92m{grid[dx][dy].strip("\033[31m").strip("\033[0m")}\033[0m"
    os.system("clear")  # noqa: S605, S607
    print("\n".join(["".join(line) for line in grid]) + f"\nScore: {min_score}")
grid[sx][sy] = f"\033[1;92m{'S'}\033[0m"
grid[ex][ey] = f"\033[1;92m{'E'}\033[0m"
os.system("clear")  # noqa: S605, S607
print("\n".join(["".join(line) for line in grid]) + f"\nScore: {min_score}")
