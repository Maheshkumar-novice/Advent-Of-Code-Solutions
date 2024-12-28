import itertools


with open('input.txt', 'r') as f:
    count = 0
    for line in f:
        chars, numbers = line.split()
        numbers = list(map(int, numbers.split(',')))
        matching_condition = ['#' * number for number in numbers]
        indices = [i for i, j in enumerate(chars) if j == '?']

        for combo in itertools.combinations(indices, sum(numbers) - chars.count('#')):
            list_chars = list(chars)
            for idx in combo:
                list_chars[idx] = '#'

            if [k for k in ''.join(list_chars).replace('?', '.').split('.') if k] == matching_condition:
                count += 1
    print(count)