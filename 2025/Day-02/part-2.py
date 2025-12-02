with open("input.txt") as f:
    input_data = list(map(lambda r: r.split("-"), f.read().split(",")))
    sum = 0
    for data in input_data:
        r = range(int(data[0]), int(data[1]) + 1)
        for i in r:
            si = str(i)
            sl = len(si)
            for j in range(1, sl // 2 + 1):
                f = False
                for k in range(1, j + 1):
                    vals = []
                    oc = ""
                    ctr = 0
                    for c in si:
                        oc += c
                        ctr += 1
                        if ctr == k:
                            ctr = 0
                            vals.append(oc)
                            oc = ""
                    if oc:
                        vals.append(oc)
                    if len(set(vals)) == 1:
                        sum += i
                        f = True
                        break
                if f:
                    break
    print(sum)
