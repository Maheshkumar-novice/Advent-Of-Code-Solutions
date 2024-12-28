total = 0


def replace_string_numbers_to_digit_numbers(string: str) -> str:
    number_string_map = {
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7', 
        'eight': '8',
        'nine': '9'
    }

    for number in number_string_map.keys():
        if number in string:
            string= string.replace(number, number + number_string_map[number] + number )

    return string


def get_two_digit_number(string: str) -> int:
    string = replace_string_numbers_to_digit_numbers(string)

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