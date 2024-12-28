with open("input.txt") as f:
    locks, keys, grid_rows = [], [], 7

    for schematic in f.read().split("\n\n"):
        grid, empty_cols = [list(line) for line in schematic.split("\n")], [0] * 5

        for idx, row in enumerate(grid):
            if all(col == "#" for col in row) and idx in (0, 6):
                lock = idx == 0
                continue

            for jdx, col in enumerate(row):
                if col == "#":
                    empty_cols[jdx] += 1

        (locks if lock else keys).append(empty_cols)

    print(sum(not any(count >= grid_rows - 1 for count in (k[0] + k[1] for k in zip(lock, key, strict=False))) for lock in locks for key in keys))
