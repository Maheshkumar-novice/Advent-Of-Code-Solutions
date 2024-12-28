with open("input.txt") as f:
    visited = set()
    current_house = (0, 0)
    visited.add(current_house)

    directions = {"^": (-1, 0), "v": (1, 0), ">": (0, 1), "<": (0, -1)}

    for direction in f.read():
        dx, dy = directions[direction]
        x, y = current_house
        current_house = x + dx, y + dy
        visited.add((x + dx, y + dy))

    print(len(visited))
