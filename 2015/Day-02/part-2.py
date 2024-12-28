import re

with open("input.txt") as f:
    result = 0
    for l, w, h in ((int(e[0]), int(e[1]), int(e[2])) for e in re.findall(r"(\d+)x(\d+)x(\d+)", f.read())):  # noqa: E741
        a, b, _ = sorted([l, w, h])
        result += a * 2 + b * 2 + (l * w * h)
    print(result)
