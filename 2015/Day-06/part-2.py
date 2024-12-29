r"""My initial Solution.

Using python arrays.

import re

with open("input.txt") as f:
    input_data = f.read()
    grid = [[0 for i in range(1000)] for j in range(1000)]

    for instruction, x_start, y_start, x_end, y_end in re.findall(r"(\w+) (?:(\d+),(\d+)) through (?:(\d+),(\d+))", input_data):
        for i in range(int(x_start), int(x_end) + 1):
            for j in range(int(y_start), int(y_end) + 1):
                if instruction == "on":
                    grid[i][j] += 1
                elif instruction == "off":
                    grid[i][j] = max(0, grid[i][j] - 1)
                elif instruction == "toggle":
                    grid[i][j] += 2

    print(sum(grid[i][j] for i in range(1000) for j in range(1000)))
"""

# Optimized solution using numpy

import re

import numpy as np

with open("input.txt") as f:
    input_data = f.read()

# Initialize grid as numpy array with integers
grid = np.zeros((1000, 1000), dtype=np.int32)

# Compile regex pattern once
pattern = re.compile(r"(?:\w+ )?(\w+) (\d+),(\d+) through (\d+),(\d+)")

# Process instructions using numpy's advanced indexing
for line in input_data.splitlines():
    match = pattern.match(line)
    if match:
        instruction, x1, y1, x2, y2 = match.groups()
        x1, y1, x2, y2 = map(int, (x1, y1, x2, y2))

        # Create view for the affected region
        region = np.s_[x1 : x2 + 1, y1 : y2 + 1]

        if instruction == "on":
            grid[region] += 1
        elif instruction == "off":
            # numpy's maximum operates element-wise
            grid[region] = np.maximum(0, grid[region] - 1)
        else:  # toggle
            grid[region] += 2

print(np.sum(grid))
