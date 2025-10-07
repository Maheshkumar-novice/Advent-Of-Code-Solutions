def is_valid_password(password: str) -> bool:  # noqa: D103
    if ("i" in password) or ("o" in password) or ("l" in password):
        return False

    three_char_flag = False
    for i in range(len(password) - 2):
        sub_str = password[i : i + 3]
        ords = [ord(char) for char in sub_str]

        if (ords[1] == ords[0] + 1) and (ords[2] == ords[1] + 1):
            three_char_flag = True
            break

    found_indices = set()
    for j in range(len(password)):
        if (j + 1) < len(password) and password[j] == password[j + 1] and j not in found_indices and (j + 1) not in found_indices:
            found_indices.add(j)
            found_indices.add(j + 1)

    return bool(len(found_indices) // 2 >= 2 and three_char_flag)  # noqa: PLR2004


with open("input.txt") as f:
    input_data = list(f.read())[::-1]

    while True:
        if is_valid_password("".join(input_data[::-1])):
            print("".join(input_data[::-1]))
            break

        for idx, char in enumerate(input_data):
            new_char = chr(ord(char) + 1)

            if char == "z":
                new_char = "a"
                input_data[idx] = new_char
                continue
            else:
                input_data[idx] = new_char
                break
