with open("input.txt") as f:
    input_data = str(f.read().strip())
    print(input_data)
    new_input_data = ""
    for _ in range(40):
        prev_char = input_data[0]
        char_count = 1
        for char in input_data[1:]:
            if prev_char == char:
                char_count += 1
                continue
            else:
                new_input_data += (str(char_count) + prev_char)
                char_count = 1
                prev_char = char
        new_input_data += str(char_count) + prev_char

        input_data = new_input_data
        new_input_data = ""
        print(_, len(input_data))
