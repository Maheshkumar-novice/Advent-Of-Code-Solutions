with open("input.txt") as f:
    data = f.read().split("\n")
    operators = data[-1]
    operators_length = len(operators) - 1
    big_index = operators_length
    total = 0
    for i in range(operators_length, -1, -1):
        if operators[i] in ("+", "*"):
            small_index = i
            operator = operators[i]
            values = []
            for index in range(big_index, small_index - 1, -1):
                value = ""
                for line in data[:-1]:
                    value += line[index]
                values.append(int(value))

            if operator == "+":
                result = sum(values)
            else:
                result = 1
                for v in values:
                    result *= v
            total += result

            big_index = small_index - 2
    print(total)
