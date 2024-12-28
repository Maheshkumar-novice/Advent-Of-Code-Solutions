from collections import defaultdict

with open('input.txt', 'r') as f:
    card_count_map = defaultdict(int)

    for line in f:
        card_number, numbers = line.strip().split(':')
        
        card_number = int(card_number.split()[-1])
        card_count_map[card_number] += 1

        winning_numbers, my_numbers = numbers.split('|')
        intersection = set(winning_numbers.split()).intersection(set(my_numbers.split()))

        for i in range(1, len(intersection) + 1):
            card_count_map[card_number + i] += card_count_map[card_number]

    print(sum(card_count_map.values()))