total = 0

def get_two_digit_number(string: str) -> int:
    numbers = []

    for char in string:
        if char.isdigit():
            numbers.append(char)

    
    if len(numbers) == 1:
        two_digit_number = numbers[0] + numbers[0]
    else:
        two_digit_number = numbers[0] + numbers[-1]

    return int(two_digit_number)

with open('input.txt', 'r') as f:
    for line in f:
        total += get_two_digit_number(line)

    print(total)