from itertools import combinations

import numpy as np


def insert_empty_row_marks(data):
    rows_to_duplicate, empty_row = [], ['.'] * len(data[0])

    for idx, i in enumerate(data):
        if all(i == '.' for i in i):
            rows_to_duplicate.append(idx)

    index = 0
    for i in rows_to_duplicate:
        data.insert(i + index, ['X'] + empty_row[1:])
        index += 1

with open('input.txt', 'r') as f:
    data = list(map(list, f.read().splitlines()))
    insert_empty_row_marks(data)

    data = np.transpose(data).tolist()
    insert_empty_row_marks(data)

    data = np.transpose(data).tolist()
    hash_coords, hash_count = {}, 0
    for idx, i in enumerate(data):
        for jdx, j in enumerate(i):
            if j == '#':
                hash_coords[hash_count + 1] = (idx, jdx)
                hash_count += 1

    total = 0
    for coords in combinations(range(1, hash_count + 1), r=2):
        x1, y1 = hash_coords[coords[0]]
        x2, y2 = hash_coords[coords[1]]
        total += abs(x1 - x2) + abs(y1 - y2)

    print(total)