import re

with open("input.txt") as f:
    vowels = {"a", "e", "i", "o", "u"}
    doubles = r"(.)\1"
    unwanted = r"(ab|cd|pq|xy)"
    print(sum(1 for string in f.read().splitlines() if not re.findall(unwanted, string) and re.findall(doubles, string) and sum(1 for char in string if char in vowels) >= 3))  # noqa: PLR2004
