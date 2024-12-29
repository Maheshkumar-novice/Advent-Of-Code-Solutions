with open("input.txt") as f:
    input_data = f.read().splitlines()

code, encoded = 0, 0
for string in input_data:
    code += len(string)
    encoded += len(string.replace("\\", "\\\\").replace('"', '\\"')) + 2
print(encoded - code)
