import pathlib
import re

print(sum(int(x) * int(y) for x, y in re.findall(r"l\((\d+),(\d+)\)", pathlib.Path("input.txt").read_text())))
