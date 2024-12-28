with open("input.txt") as f:
    input_data = f.read()

    visited = set()
    current_house = (0, 0)
    visited.add(current_house)

    directions = {"^": (-1, 0), "v": (1, 0), ">": (0, 1), "<": (0, -1)}

    # Santa
    for direction in input_data[::2]:
        dx, dy = directions[direction]
        x, y = current_house
        current_house = x + dx, y + dy
        visited.add(current_house)

    # Robo Santa
    current_house = (0, 0)
    for direction in input_data[1::2]:
        dx, dy = directions[direction]
        x, y = current_house
        current_house = x + dx, y + dy
        visited.add(current_house)

    print(len(visited))
