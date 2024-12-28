from collections import deque

with open('input.txt', 'r') as f:
    lines, moved_lines, total_load = f.read().splitlines(), [], 0
    length = len(lines)

    for line in zip(*lines):
        queue, moved_line = deque(), list(line)

        for current_thing_index, thing in enumerate(line):
            match thing:
                case 'O':
                    if queue:
                        free_space_index = queue.popleft()
                        queue.append(current_thing_index)
                    else:
                        free_space_index = current_thing_index

                    moved_line[current_thing_index], moved_line[free_space_index] = '.', 'O'
                case '.':
                    queue.append(current_thing_index)
                case '#':
                    queue.clear()
        moved_lines.append(moved_line)

    for line in zip(*moved_lines):
        total_load += (line.count('O') * length)
        length -= 1

    print(total_load)
