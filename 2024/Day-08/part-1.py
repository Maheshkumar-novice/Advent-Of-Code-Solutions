from collections import defaultdict  # noqa: D100, INP001
from itertools import combinations
from math import dist
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
        for members in antennae.values():
            for member1, member2 in combinations(members, r=2):
                distance = dist(member1, member2)
                distance2 = 2 * distance
                for i in range(len(grid)):
                    for j in range(len(grid)):
                        if grid[i][j] != "#":
                            dist1 = dist(member1, (i, j))
                            dist2 = dist(member2, (i, j))
                            d = [dist1, dist2]
                            if distance in d and distance2 in d:
                                grid[i][j] = "#"
                                result += 1
        # print(result)  # noqa: T201


def _approach_2() -> None:
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
            ax, ay = ax - dx, ay - dy
            if 0 <= ax < length and 0 <= ay < length and grid[ax][ay] != "#":
                grid[ax][ay] = "#"
                result += 1

            ax, ay = x2, y2

            ax, ay = ax + dx, ay + dy
            if 0 <= ax < length and 0 <= ay < length and grid[ax][ay] != "#":
                grid[ax][ay] = "#"
                result += 1

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

            member1 -= d  # noqa: PLW2901
            if 0 <= member1.real < length and 0 <= member1.imag < length:
                result.add(member1)

            member2 += d  # noqa: PLW2901
            if 0 <= member2.real < length and 0 <= member2.imag < length:
                result.add(member2)

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
 python3 part-1.py
291
0.22381765799946152
291
0.00031528899853583425
291
0.00039768799615558237
"""
