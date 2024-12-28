from collections import defaultdict, deque
from functools import cache
from itertools import pairwise, product

directions = {"^": (-1, 0), "v": (1, 0), ">": (0, 1), "<": (0, -1)}

KEYPAD_HEIGHT = 4
KEYPAD_WIDTH = 3
keypad = [
    ["7", "8", "9"],
    ["4", "5", "6"],
    ["1", "2", "3"],
    ["", "0", "A"],
]
keypad_index = {}
for i in range(KEYPAD_HEIGHT):
    for j in range(KEYPAD_WIDTH):
        keypad_index[keypad[i][j]] = (i, j)


@cache
def _next_keypad_directions(x: int, y: int) -> list[int]:
    next_directions = []
    for direction, (dx, dy) in directions.items():
        nx, ny = x + dx, y + dy
        if 0 <= nx < KEYPAD_HEIGHT and 0 <= ny < KEYPAD_WIDTH and keypad[nx][ny] != "":
            next_directions.append((direction, nx, ny))
    return next_directions


@cache
def _get_shortest_path_to_keypad(sx: int, sy: int, ex: int, ey: int) -> list[list[str]]:
    queue = deque([(sx, sy, 0, "", "")])
    vertice_scores = {}
    min_score = float("inf")
    score_path_map = defaultdict(list)
    while queue:
        x, y, score, path, direction = queue.popleft()
        path += direction
        if (x, y) in vertice_scores and score > vertice_scores[(x, y)]:
            continue
        vertice_scores[(x, y)] = score

        for new_direction, nx, ny in _next_keypad_directions(x, y):
            if keypad[nx][ny] == keypad[ex][ey]:
                min_score = min(score + 1, min_score)
                path += new_direction
                score_path_map[score + 1].append(path)
            else:
                queue.append((nx, ny, score + 1, path, new_direction))
    return score_path_map[min_score]


ARROW_KEYPAD_HEIGHT = 2
ARROW_KEYPAD_WIDTH = 3
arrow_keypad = [
    ["", "^", "A"],
    ["<", "v", ">"],
]
arrow_keypad_index = {}
for i in range(ARROW_KEYPAD_HEIGHT):
    for j in range(ARROW_KEYPAD_WIDTH):
        arrow_keypad_index[arrow_keypad[i][j]] = (i, j)


@cache
def _next_arrow_keypad_directions(x: int, y: int):  # noqa: ANN202
    next_directions = []
    for direction, (dx, dy) in directions.items():
        nx, ny = x + dx, y + dy
        if 0 <= nx < ARROW_KEYPAD_HEIGHT and 0 <= ny < ARROW_KEYPAD_WIDTH and arrow_keypad[nx][ny] != "":
            next_directions.append((direction, nx, ny))
    return next_directions


@cache
def _get_shortest_path_to_arrow_keypad(sx: int, sy: int, ex: int, ey: int) -> list[list[str]]:
    if arrow_keypad[sx][sy] == arrow_keypad[ex][ey]:
        return [[("", "", "")]]
    queue = deque([(sx, sy, 0, [], "")])
    vertice_scores = {}
    min_score = float("inf")
    score_path_map = defaultdict(list)
    while queue:
        x, y, score, path, direction = queue.popleft()
        path.append((x, y, direction))
        if (x, y) in vertice_scores and score > vertice_scores[(x, y)]:
            continue
        vertice_scores[(x, y)] = score

        for new_direction, nx, ny in _next_arrow_keypad_directions(x, y):
            if arrow_keypad[nx][ny] == arrow_keypad[ex][ey]:
                min_score = min(score + 1, min_score)
                score_path_map[score + 1].append([*path, (ex, ey, new_direction)])
            else:
                queue.append((nx, ny, score + 1, path.copy(), new_direction))
    return score_path_map[min_score]


@cache
def _get_arrow_result(x: int, y: int) -> list[str]:
    new = []
    another = []
    desired = ["^^", "vv", ">>", "<<"]
    flag = True
    for path in _get_shortest_path_to_arrow_keypad(*arrow_keypad_index[x], *arrow_keypad_index[y]):
        op = ""
        for _, _, direction in path:
            op += direction
        for d in desired:
            if d in op:
                another.append(op + "A")
                flag = False
        new.append(op + "A")
    return new if flag else another


with open("input.txt") as f:
    codes_str = f.read().splitlines()
    codes = ["A" + e for e in codes_str]


result = 0

for code in codes:
    paths = [[op + "A" for op in _get_shortest_path_to_keypad(*keypad_index[x], *keypad_index[y])] for x, y in pairwise(code)]
    paths = ["".join(i) for i in product(*paths)]
    min_len = min(len(e) for e in paths)
    paths = list(filter(lambda e: len(e) == min_len, paths))

    new_paths = []
    for value in paths:
        value = "A" + value  # noqa: PLW2901
        paths = []
        for x, y in pairwise(value):
            paths.append(_get_arrow_result(x, y))

        for i in product(*paths):
            c = "".join(i)
            k = c.count(">>")
            l = c.count("<<")
            m = c.count("^^")
            n = c.count("vv")
            o = k + l + m + n
            new_paths.append((c, o))

    min_len = min(len(e[0]) for e in new_paths)
    new_paths = list(filter(lambda e: len(e[0]) == min_len, new_paths))
    max_len = max(e[1] for e in new_paths)
    new_paths = list(filter(lambda e: e[1] == max_len, new_paths))

    min_ = float("inf")
    for value, _ in new_paths:
        value = "A" + value  # noqa: PLW2901
        paths = []
        for x, y in pairwise(value):
            paths.append(_get_arrow_result(x, y))
        for i in product(*paths):
            a = len("".join(i))
            min_ = min(a, min_)
    result += (min_) * int(code[1:-1])

print(result)

# print(_get_shortest_path_to_keypad.cache_info())
# print(_get_shortest_path_to_arrow_keypad.cache_info())
# print(_next_keypad_directions.cache_info())
# print(_next_arrow_keypad_directions.cache_info())
# print(_get_arrow_result.cache_info())
