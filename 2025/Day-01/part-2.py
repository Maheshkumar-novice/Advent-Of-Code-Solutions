with open("input.txt") as f:
    current = 50
    zeroes = 0
    for line in f:
        mode = line[0]
        number = int(line[1:])

        for _ in range(number):
            if mode == "L":
                current -= 1
            else:
                current += 1

            if current == -1:
                current = 99
            elif current == 100:
                current = 0

            if current == 0:
                zeroes += 1
    print(zeroes)
