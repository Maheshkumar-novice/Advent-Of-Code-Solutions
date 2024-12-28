from functools import cache

with open("input.txt") as f:
    combos, patterns = f.read().split("\n\n")
    combos = set(combos.split(", "))
    patterns = patterns.split("\n")

    @cache
    def _solve(p: str) -> bool:
        if not p:
            return 1

        c = 0
        for i in range(len(p)):
            if p[0 : i + 1] in combos:
                c += _solve(p[i + 1 :])
        return c

    print(sum(_solve(pattern) for pattern in patterns))
