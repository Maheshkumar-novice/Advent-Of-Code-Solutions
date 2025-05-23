def look_and_say(input_data, times):  # noqa: ANN001, ANN201, D103
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
    if times != 40:  # noqa: PLR2004
        return look_and_say(new_input_data, times+1)
    return new_input_data

print(len(look_and_say("1321131112", 1)))
