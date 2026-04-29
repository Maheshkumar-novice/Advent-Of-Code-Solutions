with open("input.txt") as f:
    input_data = [list(l) for l in f.read().replace("S", "|").splitlines()]
    split_count = 0
    for i, line in enumerate(input_data[1:], 1):
        for j, pos in enumerate(line):
            if pos == "." and input_data[i - 1][j] == "|":
                input_data[i][j] = "|"

            if pos == "^" and input_data[i - 1][j] == "|":
                split_count += 1
                input_data[i][j + 1] = "|"
                input_data[i][j - 1] = "|"

    for line in input_data:
        print("".join(line))
    print(split_count)
