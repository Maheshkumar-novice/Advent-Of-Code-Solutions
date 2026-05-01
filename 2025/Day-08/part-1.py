import math
from collections import defaultdict

with open("input.txt") as f:
    input_data = [list(map(int, line.split(","))) for line in f.read().splitlines()]

pair_distances = []
boss_dict = {tuple(x): tuple(x) for x in input_data}

for i in range(len(input_data)):
    for j in range(len(input_data)):
        if i != j and i < j:
            pair_distances.append((tuple(input_data[i]), tuple(input_data[j]), int(math.dist(input_data[i], input_data[j]))))  # noqa: PERF401

sorted_data = sorted(pair_distances, key=lambda e: e[2])[:1000]


def find(X):
    if boss_dict[X] == X:
        return X
    boss_dict[X] = find(boss_dict[X])
    return boss_dict[X]


def union(X, Y) -> None:
    x, y = find(X), find(Y)
    if x != y:
        boss_dict[y] = x


for jb_1, jb_2, _ in sorted_data:
    union(jb_1, jb_2)


circuits = defaultdict(list)
for box in input_data:
    box = tuple(box)
    circuits[find(box)].append(box)


r = 1
for i in sorted(circuits.values(), key=len, reverse=True)[:3]:
    r *= len(i)

print(r)
