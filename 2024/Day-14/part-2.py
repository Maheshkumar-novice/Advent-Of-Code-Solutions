import re

with open("input.txt") as f:
    values = [re.findall(r"(-?\d+),(-?\d+)", line) for line in f]
    max_x, max_y = 103, 101
    middle_x, middle_y = max_x // 2, max_y // 2
    time_elapsed = 1

    while True:
        answer_found = False
        current_positions = set()

        for position, velocity in values:
            vy, vx = int(velocity[0]) * time_elapsed, int(velocity[1]) * time_elapsed
            py, px = int(position[0]), int(position[1])
            px, py = (px + vx) % max_x, (py + vy) % max_y
            current_positions.add((px, py))

            if (px, py + 1) in current_positions and not answer_found:
                flag = True
                for i in range(2, 7):
                    new_py = py + i
                    if (px, new_py) not in current_positions:
                        flag = False
                        break
                if flag:
                    answer_found = True

        if answer_found:
            break

        time_elapsed += 1

print(time_elapsed)
