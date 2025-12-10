with open("input.txt") as f:
    ranges, _ = f.read().split("\n\n")
    ranges = [tuple(map(int, range_.strip().split("-"))) for range_ in ranges.split()]
    ranges = sorted(ranges, key=lambda x: x[0])
    result = 0
    prev_max = -1
    for x, y in ranges:
        if x <= prev_max:
            x = prev_max + 1

        if y >= x:
            result += (y - x) + 1
            prev_max = y
    print(result)
