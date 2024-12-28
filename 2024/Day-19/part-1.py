from functools import cache

with open("input.txt") as f:
    combos, patterns = f.read().split("\n\n")
    combos = set(combos.split(", "))
    patterns = patterns.split("\n")

    @cache
    def _solve(p: str) -> bool:
        if p in combos:
            return True

        return any(p[0 : i + 1] in combos and _solve(p[i + 1 :]) for i in range(len(p)))

    print(sum(_solve(pattern) for pattern in patterns))
