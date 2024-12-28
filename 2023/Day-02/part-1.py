import re

total = 0
with open('input.txt', 'r') as f:
    for line in f:
        game  = sum(int(i)       for i in re.findall(r'Game (\d+):', line))
        red   = all(int(i) <= 12 for i in re.findall(r'\d+ (?=red)', line))
        blue  = all(int(i) <= 14 for i in re.findall(r'\d+ (?=blue)', line))
        green = all(int(i) <= 13 for i in re.findall(r'\d+ (?=green)', line))

        if red and blue and green:
            total += game

    print(total)