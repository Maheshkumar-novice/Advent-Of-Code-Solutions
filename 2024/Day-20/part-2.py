from collections import deque


def get_manhattan_points(x0, y0, distance):
    # For each possible x-offset from -distance to +distance
    for dx in range(-distance, distance + 1):
        # The remaining distance must be covered by the y-coordinate
        dy = distance - abs(dx)

        # Add the point with positive dy
        yield (x0 + dx, y0 + dy)

        # Add the point with negative dy (if dy != 0)
        if dy != 0:
            yield (x0 + dx, y0 - dy)


with open("input.txt") as f:
    grid = [list(line.strip()) for line in f]
    grid_length = len(grid)
    directions = {"n": (-1, 0), "s": (1, 0), "e": (0, 1), "w": (0, -1)}
    sx, sy = next((i, j) for i in range(grid_length) for j in range(grid_length) if grid[i][j] == "S")
    ex, ey = next((i, j) for i in range(grid_length) for j in range(grid_length) if grid[i][j] == "E")
    cheat_count = 0
    possible_cheats = set()

    def _next_directions(x: int, y: int):  # noqa: ANN202
        for dx, dy in directions.values():
            nx, ny = x + dx, y + dy
            if 0 <= nx < grid_length and 0 <= ny < grid_length:
                if grid[nx][ny] != "#":
                    yield (nx, ny)
                else:
                    for i in range(1, 21):
                        for px, py in get_manhattan_points(x, y, i):
                            if 0 <= px < grid_length and 0 <= py < grid_length and grid[px][py] != "#":
                                possible_cheats.add((px, py, x, y, i))

    queue = deque([(sx, sy, 0)])
    min_score = float("inf")
    visited = set()
    while queue:
        x, y, score = queue.popleft()
        if (x, y) in visited:
            continue
        grid[x][y] = score
        visited.add((x, y))

        for nx, ny in _next_directions(x, y):
            if (nx, ny) == (ex, ey):
                min_score = min(score + 1, min_score)
            else:
                queue.append((nx, ny, score + 1))

    grid[sx][sy] = 0
    grid[ex][ey] = min_score

    for cex, cey, csx, csy, dist in possible_cheats:
        total = min_score
        dist_to_end = min_score - grid[cex][cey]
        dist_to_start = grid[csx][csy]

        saved = (total - dist_to_end - dist_to_start) - dist
        if saved >= 100:
            cheat_count += 1

    # print(min_score)
    print(cheat_count)
