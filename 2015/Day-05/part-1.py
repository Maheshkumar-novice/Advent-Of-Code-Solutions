import re

with open("input.txt") as f:
    vowels = {"a", "e", "i", "o", "u"}
    doubles = r"(.)\1"
    unwanted = r"(ab|cd|pq|xy)"
    print(sum(bool(not re.findall(unwanted, string) and re.findall(doubles, string) and sum(char in vowels for char in string) >= 3) for string in f.read().splitlines()))  # noqa: PLR2004
