with open("input.txt") as f:
    group_1 = []
    group_2 = []
    for line in f.readlines():
        a, b = line.split()
        group_1.append(int(a))
        group_2.append(int(b))

    print(sum(abs(a - b) for a, b in zip(sorted(group_1), sorted(group_2))))
