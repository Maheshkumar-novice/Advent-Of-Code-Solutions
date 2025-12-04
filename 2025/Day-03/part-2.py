def find_max_and_its_index_from_list(data):
    max_value = -1
    max_index = None
    for index, i in enumerate(data):
        if i > max_value:
            max_value = i
            max_index = index
    return max_value, max_index


with open("sample.txt") as f:
    sum_ = 0
    for line in ["234234234234278"]:
        data = list(map(int, list(line.strip())))
        replaced_count = 0
        while replaced_count != 12:
            max_value, max_index = find_max_and_its_index_from_list(data)
            big_index = len(data) - 1
            while big_index >= 0:
                if data[big_index] == max_value:
                    data[big_index] = 0
                    replaced_count += 1
                    if replaced_count == 12:
                        break
                big_index -= 1
        print(data)