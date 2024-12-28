import re

with open("input.txt") as f:
    doubles_twice = r"([a-z]{2})(.*)(\1)"
    doubles_inbetween = r"([a-z]{1})(.)(\1)"
    print(sum(bool(re.findall(doubles_twice, string) and re.findall(doubles_inbetween, string)) for string in f.read().splitlines()))
