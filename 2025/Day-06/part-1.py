with open("input.txt") as f:
    input_data = [line.strip().split() for line in f]
    from functools import reduce
    import operator
    operator_map = {'+': operator.add, '*': operator.mul}
    result = 0
    for j in range(len(input_data[0])):
        data = []
        for i in range(len(input_data)):
            data.append(input_data[i][j])
        result += reduce(operator_map[data[-1]], map(int, data[:-1]))
    print(result)
