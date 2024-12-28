from collections import deque
from functools import cache

with open('input.txt', 'r') as f:
    data = f.read().splitlines()
    row_length, column_length, result = len(data), len(data[0]), -1

    DIRECTION_MAP = {
        '|':  {'t': 't', 'b': 'b', 'r': 'tb', 'l': 'tb'},
        '-':  {'r': 'r', 'l': 'l', 't': 'rl', 'b': 'rl'},
        '\\': {'r': 'b', 'b': 'r', 't': 'l', 'l': 't'},
        '/':  {'r': 't', 't': 'r', 'l': 'b', 'b': 'l'}
    }

    DIRECTION_COORDS_UPDATE_MAP = {
        'r': (0, 1),
        'l': (0, -1),
        'b': (1, 0),
        't': (-1, 0)
    }

    @cache
    def get_move_from(direction: str, position: tuple[int]) -> list[str, tuple[int]]:
        x, y = position

        match data[x][y]:
            case '.':
                x1, y1 = DIRECTION_COORDS_UPDATE_MAP[direction]
                return [direction, ((x + x1), (y + y1))]
            case '|' | '-' as symbol:
                directions, next_moves = DIRECTION_MAP[symbol][direction], []
                for direction in directions:
                    x1, y1 = DIRECTION_COORDS_UPDATE_MAP[direction]
                    next_moves += [direction, ((x + x1), (y + y1))]
                return next_moves
            case '\\' | '/' as symbol:
                direction = DIRECTION_MAP[symbol][direction]
                x1, y1 = DIRECTION_COORDS_UPDATE_MAP[direction]
                return [direction, ((x + x1), (y + y1))]

    def move_light(direction: str, position: tuple[int]) -> None:
        queue = deque()
        queue.append((direction, position))
        visited = set()

        while queue:
            direction, position = queue.popleft()

            if (direction, position) in visited or \
               not (0 <= position[0] < row_length and 0 <= position[1] < row_length):
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

        global result
        result = max(result, len(result_set))

    # Both possibilities of edges automatically covered. i.e. top-right: right, bottom
    # top & bottom edges
    for i in range(column_length):
        move_light('b', (0, i))
        move_light('t', (row_length - 1, i))

    # right & left edges
    for i in range(row_length):
        move_light('r', (i, 0))
        move_light('l', (i, column_length - 1))
    
    print(result)
