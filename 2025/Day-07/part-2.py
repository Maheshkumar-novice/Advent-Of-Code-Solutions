with open("input.txt") as f:
    input_data = [list(l) for l in f.read().replace("S", "|").splitlines()]
    split_count = 0
    from copy import deepcopy
    def solve(input_data_copy, index):
        global split_count
        if index == len(input_data):
            return
    
        for i, line in enumerate(input_data_copy[index:], index):
            for j, pos in enumerate(line):
                if pos == "." and input_data_copy[i - 1][j] == "|":
                    if i == len(input_data_copy) - 1:
                        split_count += 1
                    input_data_copy[i][j] = "|"

                if pos == "^" and input_data_copy[i - 1][j] == "|":
                    input_data_copy[i][j + 1] = "|"
                    solve(deepcopy(input_data_copy), i + 1)
                    input_data_copy[i][j + 1] = "."

                    input_data_copy[i][j - 1] = "|"
                    solve(deepcopy(input_data_copy), i + 1)
                    input_data_copy[i][j - 1] = "."

    solve(deepcopy(input_data), 1)

    print(split_count)
