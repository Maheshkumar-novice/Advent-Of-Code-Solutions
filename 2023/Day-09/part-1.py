from itertools import pairwise

with open('input.txt', 'r') as f:
    total = 0

    for line in f:
        numbers = [int(x) for x in line.split()]
        end_of_the_sequence_value = numbers[-1]

        while True:
            numbers = [y - x for x, y in pairwise(numbers)]
            
            end_of_the_sequence_value += numbers[-1]

            if all(i == 0 for i in numbers):
                break

        total += end_of_the_sequence_value

    print(total)
