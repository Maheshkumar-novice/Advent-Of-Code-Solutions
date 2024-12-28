with open('input.txt', 'r') as f:
    sequence = f.read().strip().split(',')

    total = 0
    for seq in sequence:
        hash_start = 0
        for char in seq:
            hash_start += ord(char)
            hash_start *= 17
            hash_start %= 256
        total += hash_start
    print(total)
