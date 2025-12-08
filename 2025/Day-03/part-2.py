def find_max_and_its_index_from_list(data):
    max_value = -1
    max_index = None
    for index, i in enumerate(data):
        if i > max_value:
            max_value = i
            max_index = index
    return max_value, max_index


with open("input.txt") as f:
    sum_ = 0
    for line in f:
        data = list(map(int, list(line.strip())))
        result = []
        required_length = 12
        data_size = len(data)
        iteration_count = data_size - required_length
        while True:
            max_value, max_index = find_max_and_its_index_from_list(data[: iteration_count + 1])
            data = data[max_index + 1 :]
            required_length -= 1
            result.append(max_value)
            data_size = len(data)
            iteration_count = data_size - required_length
            if required_length == 0:
                sum_ += int("".join(map(str, result)))
                break
    print(sum_)
