from collections import defaultdict  # noqa: D100, INP001
from itertools import combinations
from time import monotonic


def _approach_1() -> None:
    with open("input.txt") as f:  # noqa: PTH123
        grid = [list(line.strip()) for line in f]
    antennae = defaultdict(list)

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] != ".":
                antennae[grid[i][j]].append((i, j))

    result = 0
    length = len(grid)
    for members in antennae.values():
        for member1, member2 in combinations(members, r=2):
            for i in range(length):
                for j in range(length):
                    if grid[i][j] != "#":
                        x1, y1 = member1
                        x2, y2 = member2
                        x3, y3 = (i, j)

                        # some collinear formula
                        if abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) == 0:
                            grid[i][j] = "#"
                            result += 1
    # print(result)  # noqa: T201


def _approach_2() -> None:  # noqa: C901, PLR0912
    # this is after i went through how other people solved it.
    with open("input.txt") as f:  # noqa: PTH123
        grid = [list(line.strip()) for line in f]
    antennae = defaultdict(list)

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] != ".":
                antennae[grid[i][j]].append((i, j))

    result = 0
    length = len(grid)
    for members in antennae.values():
        for member1, member2 in combinations(members, r=2):
            x1, y1 = member1
            x2, y2 = member2
            dx, dy = x2 - x1, y2 - y1

            ax, ay = x1, y1
            while True:
                ax, ay = ax + dx, ay + dy
                if 0 <= ax < length and 0 <= ay < length:
                    if grid[ax][ay] != "#":
                        grid[ax][ay] = "#"
                        result += 1
                else:
                    break

            ax, ay = x2, y2
            while True:
                ax, ay = ax - dx, ay - dy
                if 0 <= ax < length and 0 <= ay < length:
                    if grid[ax][ay] != "#":
                        grid[ax][ay] = "#"
                        result += 1
                else:
                    break
    # print(result)  # noqa: T201


def _approach_3() -> None:
    # this is after i went through how other people solved it.
    with open("input.txt") as f:  # noqa: PTH123
        grid = [list(line.strip()) for line in f]
    antennae = defaultdict(list)

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] != ".":
                antennae[grid[i][j]].append(i + 1j * j)

    result = set()
    length = len(grid)
    for members in antennae.values():
        for member1, member2 in combinations(members, r=2):
            d = member2 - member1

            while True:
                if 0 <= member1.real < length and 0 <= member1.imag < length:
                    result.add(member1)
                else:
                    break

                member1 += d  # noqa: PLW2901

            while True:
                if 0 <= member2.real < length and 0 <= member2.imag < length:
                    result.add(member2)
                else:
                    break

                member2 -= d  # noqa: PLW2901
    print(len(result))  # noqa: T201


s = monotonic()
_approach_1()
# print(monotonic() - s)  # noqa: T201

s = monotonic()
_approach_2()
# print(monotonic() - s)  # noqa: T201


s = monotonic()
_approach_3()
# print(monotonic() - s)  # noqa: T201


"""
 python3 part-2.py
1015
0.10931623799842782
1015
0.0005194230034248903
1015
0.001151763994130306
"""
