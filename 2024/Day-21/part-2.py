"""Solved it. This messed with my head for so long. With few hints finally found a recusive solution."""

from collections import defaultdict, deque
from functools import cache
from itertools import pairwise

DIRECTIONS = {"^": (-1, 0), "v": (1, 0), ">": (0, 1), "<": (0, -1)}
KEYPAD_HEIGHT = 4
KEYPAD_WIDTH = 3
KEYPAD = [
    ["7", "8", "9"],
    ["4", "5", "6"],
    ["1", "2", "3"],
    ["", "0", "A"],
]
KEYPAD_INDEX = {}
for i in range(KEYPAD_HEIGHT):
    for j in range(KEYPAD_WIDTH):
        KEYPAD_INDEX[KEYPAD[i][j]] = (i, j)
ARROW_KEYPAD_HEIGHT = 2
ARROW_KEYPAD_WIDTH = 3
ARROW_KEYPAD = [
    ["", "^", "A"],
    ["<", "v", ">"],
]
ARROW_KEYPAD_INDEX = {}
for i in range(ARROW_KEYPAD_HEIGHT):
    for j in range(ARROW_KEYPAD_WIDTH):
        ARROW_KEYPAD_INDEX[ARROW_KEYPAD[i][j]] = (i, j)


@cache
def _next_keypad_directions(x: int, y: int) -> list[int]:
    next_directions = []
    for direction, (dx, dy) in DIRECTIONS.items():
        nx, ny = x + dx, y + dy
        if 0 <= nx < KEYPAD_HEIGHT and 0 <= ny < KEYPAD_WIDTH and KEYPAD[nx][ny] != "":
            next_directions.append((direction, nx, ny))
    return next_directions


@cache
def _next_arrow_keypad_directions(x: int, y: int):  # noqa: ANN202
    next_directions = []
    for direction, (dx, dy) in DIRECTIONS.items():
        nx, ny = x + dx, y + dy
        if 0 <= nx < ARROW_KEYPAD_HEIGHT and 0 <= ny < ARROW_KEYPAD_WIDTH and ARROW_KEYPAD[nx][ny] != "":
            next_directions.append((direction, nx, ny))
    return next_directions


@cache
def _get_shortest_path_to_keypad(sx: int, sy: int, ex: int, ey: int) -> list[list[str]]:
    """Store all possible paths."""
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
            if KEYPAD[nx][ny] == KEYPAD[ex][ey]:
                min_score = min(score + 1, min_score)
                path += new_direction
                score_path_map[score + 1].append(path)
            else:
                queue.append((nx, ny, score + 1, path, new_direction))
    return score_path_map[min_score]


@cache
def _get_shortest_path_to_arrow_keypad(sx: int, sy: int, ex: int, ey: int) -> list[list[str]]:
    """For same position return empty. Store all possible paths."""
    if ARROW_KEYPAD[sx][sy] == ARROW_KEYPAD[ex][ey]:
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
            if ARROW_KEYPAD[nx][ny] == ARROW_KEYPAD[ex][ey]:
                min_score = min(score + 1, min_score)
                score_path_map[score + 1].append([*path, (ex, ey, new_direction)])
            else:
                queue.append((nx, ny, score + 1, path.copy(), new_direction))
    return score_path_map[min_score]


@cache
def _get_arrow_result(x: int, y: int) -> list[str]:
    """Only keep if same move repeats twice. This will always result in min score path."""
    new = []
    another = []
    desired = ["^^", "vv", ">>", "<<"]
    flag = True
    for path in _get_shortest_path_to_arrow_keypad(*ARROW_KEYPAD_INDEX[x], *ARROW_KEYPAD_INDEX[y]):
        op = ""
        for _, _, direction in path:
            op += direction
        for d in desired:
            if d in op:
                another.append(op + "A")
                flag = False
        new.append(op + "A")
    return new if flag else another


@cache
def _get_keypad_result(x: int, y: int) -> list[str]:
    new = []
    another = []
    desired = ["^^", "vv", ">>", "<<"]
    flag = True
    for path in _get_shortest_path_to_keypad(*KEYPAD_INDEX[x], *KEYPAD_INDEX[y]):
        op = path
        for d in desired:
            if d in op:
                another.append(op + "A")
                flag = False
        new.append(op + "A")
    return new if flag else another


@cache
def _do_solve_this(value: str, level: int) -> int:
    if level == 0:
        """Returning -1 because we prepend with A."""
        return len(value) - 1

    r = 0
    for x, y in pairwise(value):
        min_ = float("inf")
        for val in _get_arrow_result(x, y):
            p = _do_solve_this("A" + val, level - 1)
            min_ = min(min_, p)
        r += min_
    return r


with open("input.txt") as f:
    codes_str = f.read().splitlines()
    codes = ["A" + e for e in codes_str]


result = 0
for code in codes:
    r = 0
    first_flag = True
    for x, y in pairwise(code):
        min_ = float("inf")
        for op in _get_keypad_result(x, y):
            p = _do_solve_this("A" + op, 25)
            min_ = min(min_, p)
        r += min_
    result += r * int(code[1:-1])

print(result)

# print(_get_shortest_path_to_keypad.cache_info())
# print(_get_shortest_path_to_arrow_keypad.cache_info())
# print(_next_keypad_directions.cache_info())
# print(_next_arrow_keypad_directions.cache_info())
# print(_get_arrow_result.cache_info())
# print(_do_solve_this.cache_info())
