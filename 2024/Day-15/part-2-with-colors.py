class Box:  # noqa: D101
    def __init__(self, start: tuple[int, int], end: tuple[int, int]) -> None:  # noqa: D107
        self.start = start
        self.end = end

    def __str__(self) -> str:  # noqa: D105
        return f"Box<{self.start} {self.end}>"

    def __repr__(self) -> str:  # noqa: D105
        return f"Box<{self.start} {self.end}>"

    def __lt__(self, other: "Box") -> bool:  # noqa: D105
        return self.start < other.start


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


with open("input.txt") as f:
    map_, directions = f.read().split("\n\n")
    map_ = map_.replace("#", "##")
    map_ = map_.replace("O", "[]")
    map_ = map_.replace(".", "..")
    map_ = map_.replace("@", "@.")
    grid = [list(line) for line in map_.split()]
    movements = {"<": (0, -1), ">": (0, 1), "^": (-1, 0), "v": (1, 0)}
    box_map = {}

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "@":
                x, y = (i, j)

            if grid[i][j] == "[" and grid[i][j + 1] == "]":
                box = Box((i, j), (i, j + 1))
                box_map[(i, j)] = box
                box_map[(i, j + 1)] = box

    counter = 0
    for movement in directions:
        counter += 1
        if movement not in movements:
            continue

        dx, dy = movements[movement]
        new_x, new_y = x + dx, y + dy

        symbol = grid[new_x][new_y]

        if symbol == ".":
            grid[new_x][new_y], grid[x][y], x, y = "@", ".", new_x, new_y
        elif symbol in ("[", "]"):
            box = box_map[(new_x, new_y)]
            to_move = [box]
            q = [box.start, box.end]
            while q:
                nx, ny = q.pop()
                nx, ny = nx + dx, ny + dy
                if grid[nx][ny] in ("[", "]"):
                    next_box = box_map[(nx, ny)]
                    if next_box not in to_move:
                        q.append(next_box.start)
                        q.append(next_box.end)
                        to_move.append(next_box)

            if movement in ("<", "^"):
                to_move = sorted(to_move)
            elif movement in (">", "v"):
                to_move = sorted(to_move, reverse=True)

            possible_to_move = True
            for box in to_move:
                sx, sy = box.start
                ex, ey = box.end

                nsx, nsy = sx + dx, sy + dy
                nex, ney = ex + dx, ey + dy

                if grid[nsx][nsy] == "#" or grid[nex][ney] == "#":
                    possible_to_move = False
                    break

            if possible_to_move:
                for box in to_move:
                    sx, sy = box.start
                    ex, ey = box.end

                    nsx, nsy = sx + dx, sy + dy
                    nex, ney = ex + dx, ey + dy

                    box.start = (nsx, nsy)
                    box.end = (nex, ney)

                    del box_map[(sx, sy)]
                    del box_map[(ex, ey)]

                    box_map[(nsx, nsy)] = box
                    box_map[(nex, ney)] = box

                    ps, pe = grid[sx][sy], grid[ex][ey]
                    grid[sx][sy], grid[ex][ey] = ".", "."
                    grid[nsx][nsy], grid[nex][ney] = ps, pe

                grid[new_x][new_y] = "@"
                grid[x][y] = "."
                x, y = new_x, new_y

        # naive visualisation
        import os

        r = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "[":
                    box = box_map[(i, j)]
                    r += 100 * box.start[0] + box.start[1]
        print("\n".join(["".join(colorize(line)) for line in grid]) + f"\nScore: {next(colorize(str(r)))} Direction: {next(colorize(movement))} Iteration: {next(colorize(str(counter)))}")
        from time import sleep

        sleep(0.1)
        os.system("clear")  # noqa: S605, S607

    r = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "[":
                box = box_map[(i, j)]
                r += 100 * box.start[0] + box.start[1]
    print(r)
