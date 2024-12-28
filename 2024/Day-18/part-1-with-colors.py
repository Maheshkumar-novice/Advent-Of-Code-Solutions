import os
import re
from collections import deque


def colorize(line):  # noqa: ANN001, ANN201, D103
    BLUE = "\033[34m"  # noqa: N806
    RESET = "\033[0m"  # noqa: N806
    ORANGE = "\033[1;38;5;208m"  # noqa: N806
    BOLD_RED = "\033[31m"  # noqa: N806
    BLUE = "\033[34m"  # noqa: N806
    BOLD_GREEN = "\033[1;92m"  # noqa: N806
    BRIGHT_YELLOW = "\033[93m"  # noqa: N806

    if isinstance(line, str):
        yield f"{BRIGHT_YELLOW}{line}{RESET}"

    for l in line:  # noqa: E741
        if l == "#":
            yield f"{BOLD_RED}#{RESET}"
        elif l == ".":
            yield f"{BLUE}.{RESET}"
        elif l == "@":
            yield f"{BOLD_GREEN}@{RESET}"
        else:
            yield f"{ORANGE}{l}{RESET}"


def bfs() -> None:  # noqa: D103
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
        vertice_scores = {}
        while queue:
            x, y, score = queue.popleft()
            grid[x][y] = "O"
            if (x, y) in vertice_scores and score >= vertice_scores[(x, y)]:
                continue
            vertice_scores[(x, y)] = score

            for nx, ny in _next_directions(x, y):
                if (nx, ny) == (grid_length - 1, grid_length - 1):
                    min_score = min(score + 1, min_score)
                else:
                    queue.append((nx, ny, score + 1))
            print("\n".join(["".join(colorize(line)) for line in grid]))
            os.system("clear")  # noqa: S605, S607
        print(min_score)


def dfs() -> None:  # noqa: D103
    with open("sample.txt") as f:
        import sys

        sys.setrecursionlimit(1500)
        grid_length = 7
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

        for x, y in memory_bytes[:12]:
            grid[x][y] = "#"
        print("\n".join(["".join(colorize(line)) for line in grid]))

        def run_dfs(x, y, score, visited_scores):  # noqa: ANN001, ANN202
            if (x, y) == (grid_length - 1, grid_length - 1):
                return score

            if (x, y) in visited_scores and score >= visited_scores[(x, y)]:
                return float("inf")

            visited_scores[(x, y)] = score
            print("\n".join(["".join(colorize(line)) for line in grid]))
            os.system("clear")  # noqa: S605, S607
            grid[x][y] = "O"

            best_score = float("inf")
            for nx, ny in _next_directions(x, y):
                new_score = run_dfs(nx, ny, score + 1, visited_scores)

                best_score = min(new_score, best_score)

            return best_score

        print(run_dfs(0, 0, 0, {}))

    print("\n".join(["".join(colorize(line)) for line in grid]))


bfs()
dfs()
