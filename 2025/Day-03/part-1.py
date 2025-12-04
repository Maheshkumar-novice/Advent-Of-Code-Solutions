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
        max_value, max_index = find_max_and_its_index_from_list(data)
        if max_index == len(data) - 1:
            second_max_value, second_max_index = find_max_and_its_index_from_list(data[:max_index])
            sum_ += int(f"{second_max_value}{max_value}")
        else:
            second_max_value, second_max_index = find_max_and_its_index_from_list(data[max_index + 1 :])
            sum_ += int(f"{max_value}{second_max_value}")
    print(sum_)
