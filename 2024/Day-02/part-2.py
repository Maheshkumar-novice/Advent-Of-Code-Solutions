with open("input.txt") as f:
    reports = [list(map(int, line.split())) for line in f]


def is_safe(report: list, ignore_idx: int) -> bool:
    desc, asc, prev = False, False, None

    for idx, level in enumerate(report):
        if idx == ignore_idx:
            continue

        if not prev:
            prev = level
            continue

        if prev < level:
            asc = True
        elif prev > level:
            desc = True

        if (prev == level) or abs(prev - level) > 3 or (asc and desc):
            return False

        prev = level
    return True


print(sum(any(is_safe(report, i) for i in range(len(report))) for report in reports))
