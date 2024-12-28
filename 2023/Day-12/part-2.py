from functools import cache

@cache
def get_answer(chars, numbers, groups_size=0):
    if not chars:
        if (len(numbers) == 1 and numbers[0] == groups_size) or (len(numbers) == 0 and groups_size == 0):
            return 1
        return 0

    char = chars[0]
    chars = chars[1:]
    clue, *new_clues = numbers or [0]
    new_clues = tuple(new_clues)

    if char == '?':
        return get_answer('#' + chars, numbers, groups_size) + get_answer('.' + chars, numbers, groups_size)
    elif char == '#':
        return 0 if groups_size > clue else get_answer(chars, numbers, groups_size + 1)
    elif char == '.':
        if groups_size == 0:
            return get_answer(chars, numbers, 0)
        elif groups_size == clue:
            return get_answer(chars, new_clues, 0)
        return 0

with open('input.txt', 'r') as f:
    count = 0
    for line in f:
        chars, numbers = line.split()

        chars_temp = chars
        for i in range(4):
            chars += ('?' + chars_temp)
    
        numbers = tuple(map(int, numbers.split(','))) * 5

        count += (get_answer(''.join(chars), numbers))
        # print(get_answer.cache_info())
    print(count)