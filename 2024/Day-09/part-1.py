from collections.abc import Generator  # noqa: INP001, D100
from time import monotonic
from typing import Any

s = monotonic()
with open("input.txt") as f:  # noqa: PTH123
    disk_map = f.read().strip()

    expanded_disk_map, free_space, ident = [], False, 0
    for thing in disk_map:
        if free_space:
            for _ in range(int(thing)):
                expanded_disk_map.append(".")  # noqa: PERF401
        else:
            for _ in range(int(thing)):
                expanded_disk_map.append(str(ident))  # noqa: PERF401
            ident += 1
        free_space = not free_space

    def _next_free_space() -> Generator[tuple[int, int, int], Any, None]:
        free = 0
        for idx, char in enumerate(expanded_disk_map):
            if char == ".":
                free += 1
                continue

            if free:
                yield (idx - free, idx - 1, free)
            free = 0

    free_space_iter = _next_free_space()
    blocks = reversed(expanded_disk_map)

    block_idx = len(expanded_disk_map) - 1

    block = next(blocks)
    start, end, space = next(free_space_iter)
    while True:
        if start > block_idx:
            break

        expanded_disk_map[start], expanded_disk_map[block_idx] = block, "."

        start += 1
        space -= 1

        block = next(blocks)
        block_idx -= 1
        while block == ".":
            block = next(blocks)
            block_idx -= 1

        if not space:
            start, end, space = next(free_space_iter, (None,) * 3)

        if space is None:
            break

    print(sum(int(char) * idx for idx, char in enumerate(expanded_disk_map) if char != "."))  # noqa: T201
# print(monotonic() - s)  # noqa: T201

"""
0.039413958991644904
"""
