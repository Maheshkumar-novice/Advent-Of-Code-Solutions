import dis

# For the iterative version
def iterative_version():
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
    return len(input_data)

# For the recursive version
def recursive_version():
    def look_and_say(input_data, times):
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
    
    return len(look_and_say("1321131112", 1))

# Disassemble both functions to see their bytecode
print("ITERATIVE VERSION BYTECODE:")
dis.dis(iterative_version)

print("\nRECURSIVE VERSION BYTECODE:")
dis.dis(recursive_version)

# You may also want to look specifically at the inner function in the recursive version
# print("\nINNER RECURSIVE FUNCTION BYTECODE:")
# inner_func = recursive_version.__code__.co_consts[1]  # This gets the code object for look_and_say
# dis.dis(inner_func)