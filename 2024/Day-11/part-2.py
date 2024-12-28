from functools import cache  # noqa: D100, INP001
from time import monotonic

s = monotonic()
with open("input.txt") as f:  # noqa: PTH123

    @cache
    def _apply_rule(stone: str, blink: int) -> int:
        if blink <= 0:
            return 1

        if stone == "0":
            return _apply_rule("1", blink - 1)

        if len(stone) % 2 == 0:
            return _apply_rule(str(int(stone[: len(stone) // 2])), blink - 1) + _apply_rule(str(int(stone[len(stone) // 2 :])), blink - 1)

        return _apply_rule(str(int(stone) * 2024), blink - 1)

    print(f"{sum(_apply_rule(stone, 75) for stone in f.read().split()):,}")  # noqa: T201

"""
0.08001491700997576
"""
