input_data = "1321131112"
for _ in range(40):
    new_input_data = ""
    char_count = 1
    prev_char = input_data[0]
    i = 1
    len_ = len(input_data)
    while i < len_:
        if input_data[i] == prev_char:
            char_count += 1
        else:
            new_input_data += str(char_count) + prev_char
            char_count = 1
        prev_char = input_data[i]
        i += 1
    new_input_data += str(char_count) + prev_char
    input_data = new_input_data
print(len(input_data))
