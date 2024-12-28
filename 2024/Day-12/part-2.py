with open("input.txt") as f:
    garden = [list(line.strip()) for line in f]
    directions = {"d": (1, 0), "u": (-1, 0), "r": (0, 1), "l": (0, -1)}
    diagonal_directions = {"tr": (-1, 1), "tl": (-1, -1), "br": (1, 1), "bl": (1, -1)}

    class Plot:  # noqa: D101
        def __init__(self, x: int, y: int) -> None:  # noqa: D107
            self.x = x
            self.y = y
            self.weight = 0
            self.fences = set()

        def __str__(self) -> str:  # noqa: D105
            return f"Plot<{garden[self.x][self.y]}, {self.x=}, {self.y=}, {self.weight=}, {sorted(self.fences)!s}>"

    def _in_bound(x: int, y: int) -> bool:
        return 0 <= x < len(garden) and 0 <= y < len(garden)

    def _get_neighbour_plot(x: int, y: int):  # noqa: ANN202
        for dx, dy in directions.values():
            new_x, new_y = x + dx, y + dy
            if _in_bound(new_x, new_y):
                yield new_x, new_y

    def _get_diagonal_neighbour_plot(x: int, y: int):  # noqa: ANN202
        for dir, (dx, dy) in diagonal_directions.items():  # noqa: A001
            new_x, new_y = x + dx, y + dy
            if _in_bound(new_x, new_y):
                yield dir, new_x, new_y

    plot_map = {}
    for i in range(len(garden)):
        for j in range(len(garden)):
            plot = Plot(i, j)
            fences = set()
            diagonal_connection_directions = set()

            for direction, (dx, dy) in directions.items():
                new_x, new_y = i + dx, j + dy
                if _in_bound(new_x, new_y):
                    if garden[new_x][new_y] == garden[i][j]:
                        continue
                    else:
                        fences.add(direction)
                else:
                    fences.add(direction)

            if len(fences) == 4:  # noqa: PLR2004
                plot.weight = 4
            elif len(fences) == 3:  # noqa: PLR2004
                plot.weight = 2

                if "u" in fences and "d" in fences and "l" in fences:
                    diagonal_connection_directions = {"l"}
                elif "u" in fences and "d" in fences and "r" in fences:
                    diagonal_connection_directions = {"r"}
                elif "l" in fences and "r" in fences and "u" in fences:
                    diagonal_connection_directions = {"u"}
                elif "l" in fences and "r" in fences and "d" in fences:
                    diagonal_connection_directions = {"d"}
            elif len(fences) == 2:  # noqa: PLR2004
                if ("u" in fences and "d" not in fences) or ("d" in fences and "u" not in fences):
                    plot.weight = 1

                if "u" in fences and "l" in fences:
                    diagonal_connection_directions = {"l", "u"}
                elif "u" in fences and "r" in fences:
                    diagonal_connection_directions = {"r", "u"}
                elif "d" in fences and "l" in fences:
                    diagonal_connection_directions = {"l", "d"}
                elif "d" in fences and "r" in fences:
                    diagonal_connection_directions = {"r", "d"}
                elif "u" in fences and "d" in fences:
                    diagonal_connection_directions = {"l", "r"}
                elif "l" in fences and "r" in fences:
                    diagonal_connection_directions = {"u", "d"}
            elif len(fences) == 1:
                if "u" in fences or "d" in fences:
                    diagonal_connection_directions = {"l", "r"}
                elif "l" in fences or "r" in fences:
                    diagonal_connection_directions = {"u", "d"}

            plot.diagonal_connection_directions = diagonal_connection_directions
            plot.fences = fences
            plot_map[(i, j)] = plot

    r = 0
    global_visited = set()
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

            a = 0
            visited_diagonal_matches = set()
            for x, y in visited:
                global_visited.add((x, y))
                plot = plot_map[(x, y)]

                if len(plot.fences) < 4:  # noqa: PLR2004
                    for dir, dx, dy in _get_diagonal_neighbour_plot(plot.x, plot.y):  # noqa: A001
                        if garden[dx][dy] == garden[plot.x][plot.y] and (dx, dy) in visited:
                            target = plot_map[(dx, dy)]
                            diagonal_match = plot.diagonal_connection_directions.intersection(target.fences)

                            if len(plot.fences) != 3:  # noqa: PLR2004
                                if (plot.x, plot.y, dx, dy) in visited_diagonal_matches:
                                    continue
                                elif "d" in plot.fences and dir in ["bl", "br"]:
                                    if diagonal_match and dir == "bl" and "r" in diagonal_match:
                                        plot.weight += 1
                                    if diagonal_match and dir == "br" and "l" in diagonal_match:
                                        plot.weight += 1
                                elif "u" in plot.fences and dir in ["tl", "tr"]:
                                    if diagonal_match and dir == "tl" and "r" in diagonal_match:
                                        plot.weight += 1
                                    if diagonal_match and dir == "tr" and "l" in diagonal_match:
                                        plot.weight += 1
                                elif "l" in plot.fences and dir in ["tl", "bl"]:
                                    if diagonal_match and dir == "tl" and "d" in diagonal_match:
                                        plot.weight += 1
                                    if diagonal_match and dir == "bl" and "u" in diagonal_match:
                                        plot.weight += 1
                                elif "r" in plot.fences and dir in ["tr", "br"]:
                                    if diagonal_match and dir == "tr" and "d" in diagonal_match:
                                        plot.weight += 1
                                    if diagonal_match and dir == "br" and "u" in diagonal_match:
                                        plot.weight += 1

                                visited_diagonal_matches.add((dx, dy, plot.x, plot.y))
                            else:
                                if (plot.x, plot.y, dx, dy) in visited_diagonal_matches:
                                    continue
                                elif (
                                    ("u" in plot.fences and "d" in plot.fences and "l" in plot.fences and dir in ["tr", "br"] and diagonal_match)
                                    or ("u" in plot.fences and "d" in plot.fences and "r" in plot.fences and dir in ["tl", "bl"] and diagonal_match)
                                    or ("l" in plot.fences and "r" in plot.fences and "u" in plot.fences and dir in ["br", "bl"] and diagonal_match)
                                    or ("l" in plot.fences and "r" in plot.fences and "d" in plot.fences and dir in ["tr", "tl"] and diagonal_match)
                                ):
                                    plot.weight += 1
                                visited_diagonal_matches.add((dx, dy, plot.x, plot.y))

                a += plot.weight
            r += a * len(visited)
print(r)
