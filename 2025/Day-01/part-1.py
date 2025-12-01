with open("input.txt") as f:
    current = 50
    zeroes = 0
    for line in f:
        mode = line[0]
        number = int(line[1:])
        new_value = current - number if mode == "L" else current + number
        mod_value = new_value % 100

        current = mod_value

        if current == 0:
            zeroes += 1
    print(zeroes)
