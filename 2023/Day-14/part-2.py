from collections import defaultdict, deque


def tilt(data):
    moved_lines = []
    for line in data:
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
                    queue = deque()
        moved_lines.append(moved_line)
    return moved_lines


with open('input.txt', 'r') as f:
    lines, total_load, i, LEN = f.read().splitlines(), 0, 0, 1_000_000_000
    cycle_cache, cycle_start, cycle_end, repeat_data = defaultdict(int), -1, -1, []
    length = len(lines)
   
    while i < LEN:
        # north
        lines = tilt([*zip(*lines)])
        lines = [*zip(*lines)]

        # west
        lines = tilt(lines)

        # south
        lines = [*zip(*lines)]
        lines = [line[::-1] for line in lines]
        lines = tilt(lines)
        lines = [line[::-1] for line in lines]
        lines = [*zip(*lines)]

        # east
        lines = tilt([line[::-1] for line in lines])
        lines = [line[::-1] for line in lines]

        key = str(lines)
        cycle_cache[key] += 1

        if cycle_cache[key] == 2:
            repeat_data.append(lines)

            if cycle_start == -1:
                cycle_start = i

        if cycle_cache[key] == 3:
            if cycle_end == -1:
                cycle_end = i
            break
        i += 1
    
    repeat = cycle_end - cycle_start
    last_cycle = repeat_data[(LEN - cycle_start) % repeat - 1]
    for line in last_cycle:
        total_load += (line.count('O') * length)
        length -= 1

    print(total_load)
