import re
from collections import deque

PIPE_MATCH_MAP = {
    '|': {
        'top': {'|', '7', 'F'},
        'bottom': {'L', 'J', '|'},
        'right': {},
        'left': {}
    },
    '-': {
        'top': {},
        'bottom': {},
        'right': {'7', 'J', '-'},
        'left': {'F', 'L', '-'}
    },
    'L': {
        'top': {'7', 'F', '|'},
        'bottom': {},
        'right': {'-', 'J', '7'},
        'left': {}
    },
    'J': {
        'top': {'|', 'F', '7'},
        'bottom': {},
        'right': {},
        'left': {'-', 'F', 'L'}
    },
    '7': {
        'top': {},
        'bottom': {'J', '|', 'L'},
        'right': {},
        'left': {'-', 'F', 'L'}
    },
    'F': {
        'top': {},
        'bottom': {'|', 'L', 'J'},
        'right': {'-', 'J', '7'},
        'left': {}
    }
}


def get_connections(coords, data, row_length, column_length):
    top = (coords[0] - 1, coords[1])
    bottom = (coords[0] + 1, coords[1])
    right = (coords[0], coords[1] + 1)
    left = (coords[0], coords[1] - 1)

    if not (top[0] >= 0 and top[1] >= 0):
        top = None

    if not (bottom[0] >=0 and bottom[1] >= 0 and bottom[0] < column_length):
        bottom = None

    if not (right[0] >= 0 and right[1] >= 0 and right[1] < row_length):
        right = None

    if not (left[0] >= 0 and left[1] >= 0):
        left = None

    top_connectable, bottom_connectable, right_connectable, left_connectable = None, None, None, None

    symbol = data[coords[0]][coords[1]]

    if top and data[top[0]][top[1]] in PIPE_MATCH_MAP[symbol]['top']:
        top_connectable = top

    if bottom and data[bottom[0]][bottom[1]] in PIPE_MATCH_MAP[symbol]['bottom']:
        bottom_connectable = bottom

    if right and data[right[0]][right[1]] in PIPE_MATCH_MAP[symbol]['right']:
        right_connectable = right

    if left and data[left[0]][left[1]] in PIPE_MATCH_MAP[symbol]['left']:
        left_connectable = left

    return top_connectable, bottom_connectable, right_connectable, left_connectable


with open('input.txt', 'r') as f:
    file_contents = f.read()

    s_place = re.search(r'S', file_contents)
    s_index_start = s_place.span()[0]

    data = file_contents.splitlines()
    row_length = len(data[0])
    column_length = len(data)

    s_index = (s_index_start // row_length, s_index_start - ((s_index_start // row_length) * (row_length + 1)))

    for idx, i in enumerate(data):
       data[idx] = list(i)

    for i in ['|', '-', 'F', '7', 'J', 'L']:
        data[s_index[0]][s_index[1]] = i

        counter = 0
        for i in get_connections(s_index, data, row_length, column_length):
            if i:
                counter += 1

        if counter == 2:
            break

    queue = deque()
    queue.append(s_index)

    main_loop = set()
    count_map = {s_index: 0}

    while queue:
        pipe = queue.popleft()

        if (pipe in main_loop) or (data[pipe[0]][pipe[1]] == '.'):
            continue

        for i in get_connections(pipe, data, row_length, column_length):
            if i and i not in main_loop:
                queue.append(i)
                count_map[i] = count_map[pipe] + 1

        main_loop.add(pipe)

    print(max(count_map.values()))