with open("input.txt") as f:
    reports = [list(map(int, line.split())) for line in f]


def is_safe(report: list) -> bool:
    desc, asc, prev = False, False, report[0]

    for idx in range(1, len(report)):
        level = report[idx]

        if prev < level:
            asc = True
        elif prev > level:
            desc = True

        if (prev == level) or abs(prev - level) > 3 or (asc and desc):
            return False

        prev = level
    return True


print(sum(is_safe(report) for report in reports))
