import re

with open("input.txt") as f:
    input_data = f.read().splitlines()

code, memory = 0, 0
pattern = re.compile(r"(\\x[0-9a-f]{2})|(\\.{1})")
for string in input_data:
    code += len(string)
    memory += len(pattern.sub(".", string).replace('"', ""))
print(code - memory)
