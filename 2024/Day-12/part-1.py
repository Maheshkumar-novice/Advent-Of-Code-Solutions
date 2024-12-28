from collections.abc import Generator
from typing import Any

with open("input.txt") as f:
    garden = [list(line.strip()) for line in f]
    directions = {
        "right": (1, 0),
        "left": (-1, 0),
        "up": (0, 1),
        "down": (0, -1),
    }

    def _in_bound(x: int, y: int) -> bool:
        return 0 <= x < len(garden) and 0 <= y < len(garden)

    def _get_neighbour_area(x: int, y: int) -> Generator[tuple[int, int], Any, None]:
        for dx, dy in directions.values():
            new_x, new_y = x + dx, y + dy
            if _in_bound(new_x, new_y):
                if garden[new_x][new_y] == garden[x][y]:
                    yield 0
                else:
                    yield 1
            else:
                yield 1

    def _get_neighbour_plot(x: int, y: int) -> Generator[tuple[int, int], Any, None]:
        for dx, dy in directions.values():
            new_x, new_y = x + dx, y + dy
            if _in_bound(new_x, new_y):
                yield new_x, new_y

    garden_plot_area = [[0 for _ in range(len(garden))] for _ in range(len(garden[0]))]
    for i in range(len(garden)):
        for j in range(len(garden)):
            plot = garden[i][j]

            plot_area = 0
            for area in _get_neighbour_area(i, j):
                plot_area += area
            garden_plot_area[i][j] = plot_area

    global_visited = set()
    r = 0
    for i in range(len(garden)):
        for j in range(len(garden[0])):
            if (i, j) in global_visited:
                continue

            visited = set()
            q = set()
            q.add((i, j))
            while q:
                x, y = q.pop()
                visited.add((x, y))

                for new_x, new_y in _get_neighbour_plot(x, y):
                    if garden[new_x][new_y] == garden[x][y] and (new_x, new_y) not in visited:
                        q.add((new_x, new_y))

            a = len(visited)
            r += sum(garden_plot_area[kk][ll] for kk, ll in visited) * a
            for x, y in visited:
                global_visited.add((x, y))
    print(r)
