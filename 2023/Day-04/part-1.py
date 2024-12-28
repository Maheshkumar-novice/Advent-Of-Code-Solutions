with open('input.txt', 'r') as f:
    total = 0

    for line in f:
        winning_numbers, my_numbers = line.strip().split(':')[-1].split('|')
        intersection = set(winning_numbers.split()).intersection(set(my_numbers.split()))
        total += int(2 ** (len(intersection) - 1))

    print(total)
