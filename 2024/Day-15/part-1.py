with open("input.txt") as f:
    map_, paths = f.read().split("\n\n")
    grid = [list(line) for line in map_.split()]
    movements = {"<": (0, -1), ">": (0, 1), "^": (-1, 0), "v": (1, 0)}

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "@":
                x, y = (i, j)
                break

    for movement in paths:
        if movement not in movements: continue  # noqa: E701

        dx, dy = movements[movement]
        new_x, new_y = x + dx, y + dy

        symbol = grid[new_x][new_y]
        if symbol == "#":
            continue
        elif symbol == ".":
            grid[new_x][new_y] = "@"
            grid[x][y] = "."
            x, y = new_x, new_y
        elif symbol == "O":
            to_move = [(new_x, new_y)]
            o_new_x, o_new_y = new_x, new_y
            while True:
                o_new_x, o_new_y = o_new_x + dx, o_new_y + dy
                o_symbol = grid[o_new_x][o_new_y]
                if o_symbol in (".", "#"):
                    break
                to_move.append((o_new_x, o_new_y))

            flag = True
            for a, b in reversed(to_move):
                new_a, new_b = a + dx, b + dy
                if grid[new_a][new_b] == "#":
                    flag = False
                    break
                grid[new_a][new_b] = "O"
                grid[a][b] = "."
            if flag:
                grid[new_x][new_y] = "@"
                grid[x][y] = "."
                x, y = new_x, new_y

    r = 0
    for i in range(len(grid)):
        for j in range(len(grid)):
            if grid[i][j] == "O":
                r += 100 * i + j
    print(r)
