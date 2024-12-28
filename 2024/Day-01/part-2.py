with open("input.txt") as f:
    group_1 = []
    group_2 = []
    for line in f.readlines():
        a, b = line.split()
        group_1.append(int(a))
        group_2.append(int(b))

    from collections import Counter

    group_2_count = Counter(group_2)

    print(sum(i * group_2_count.get(i, 0) for i in group_1))
