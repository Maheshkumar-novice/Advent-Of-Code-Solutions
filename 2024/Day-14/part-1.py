import re

with open("input.txt") as f:
    values = [re.findall(r"(-?\d+),(-?\d+)", line) for line in f]
    max_x, max_y = 103, 101
    middle_x, middle_y = max_x // 2, max_y // 2
    q1, q2, q3, q4 = 0, 0, 0, 0

    for position, velocity in values:
        vy, vx = int(velocity[0]) * 100, int(velocity[1]) * 100
        py, px = int(position[0]), int(position[1])
        px, py = (px + vx) % max_x, (py + vy) % max_y

        if 0 <= px < middle_x and 0 <= py < middle_y:
            q1 += 1
        elif 0 <= px < middle_x and middle_y < py < max_y:
            q2 += 1
        elif middle_x < px < max_x and 0 <= py < middle_y:
            q3 += 1
        elif middle_x < px < max_x and middle_y < py < max_y:
            q4 += 1

    print(q1 * q2 * q3 * q4)
