from time import monotonic  # noqa: D100, INP001

s = monotonic()
with open("input.txt") as f:  # noqa: PTH123
    stones = f.read().split()

    def _apply_rule(stone: str):  # noqa: ANN202
        if stone == "0":
            yield "1"
        elif len(stone) % 2 == 0:
            yield str(int(stone[: len(stone) // 2]))
            yield str(int(stone[len(stone) // 2 :]))
        else:
            yield str(int(stone) * 2024)

    for i in range(25):
        stones = [i for stone in stones for i in _apply_rule(stone)]
    print(f"{len(stones):,}")  # noqa: T201

"""
0.11531575000844896
"""
