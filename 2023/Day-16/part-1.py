from collections import deque

with open('input.txt', 'r') as f:
    data = f.read().splitlines()
    row_length, column_length = len(data), len(data[0])

    DIRECTION_MAP = {
        '|':  {'t': 't', 'b': 'b', 'r': 'tb', 'l': 'tb'},
        '-':  {'r': 'r', 'l': 'l', 't': 'rl', 'b': 'rl'},
        '\\': {'r': 'b', 'b': 'r', 't': 'l', 'l': 't'},
        '/':  {'r': 't', 't': 'r', 'l': 'b', 'b': 'l'}
    }

    def is_valid_position(x: int, y: int) -> bool:
        return not (x >= row_length or x < 0 or y >= column_length or y < 0)
    
    def get_direction_coords(direction: str, position: tuple[int]) -> tuple[int]:
        match direction:
            case 'r':
                return (position[0], position[1] + 1)
            case 'l':
                return (position[0], position[1] - 1)
            case 'b':
                return (position[0] + 1, position[1])
            case 't':
                return (position[0] - 1, position[1])

    def get_move_from(direction: str, position: tuple[int]) -> list[str, tuple[int]]:
        match data[position[0]][position[1]]:
            case '.':
                return [direction, get_direction_coords(direction, position)]
            case '|' | '-' as symbol:
                directions = DIRECTION_MAP[symbol][direction]
                next_moves = []
                for direction in directions:
                    next_moves += [direction, get_direction_coords(direction, position)]
                return next_moves
            case '\\' | '/' as symbol:
                direction = DIRECTION_MAP[symbol][direction]
                return [direction, get_direction_coords(direction, position)]

    queue = deque()
    queue.append(('r', (0, 0)))
    visited = set()

    while queue:
        direction, position = queue.popleft()

        if (direction, position) in visited or not is_valid_position(*position) :
            continue

        match get_move_from(direction, position):
            case d1, p1:
                queue.append((d1, p1))
            case d1, p1, d2, p2:
                queue.append((d1, p1))
                queue.append((d2, p2))

        visited.add((direction, position))

    result_set = set()
    for _, p in visited:
        result_set.add(p)

    print(len(result_set))