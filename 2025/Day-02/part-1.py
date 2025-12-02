with open("input.txt") as f:
    input_data = list(map(lambda r: r.split("-"), f.read().split(",")))
    sum = 0
    for data in input_data:
        r = range(int(data[0]), int(data[1]) + 1)
        for i in r:
            si = str(i)
            if si[: len(si) // 2] == si[len(si) // 2 :]:
                sum += i

    print(sum)
