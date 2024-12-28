import re
from time import monotonic

import numpy as np

st = monotonic()
with open("input.txt") as f:
    all_details = [list(map(int, re.findall(r"\d+", line))) for line in f.read().split("\n\n")]

    tokens = 0
    for detail in all_details:
        # solve: x*(const) + y*(const) = const  # noqa: ERA001
        equations = np.array([[detail[0], detail[2]], [detail[1], detail[3]]])
        constants = np.array(detail[4:])
        x, y = np.linalg.solve(equations, constants)
        x, y = round(x, 3), round(y, 3)  # floating precision issue resolution

        #  to make sure our results are ints and not with decimal values and max value
        if (np.mod(x, 1) == 0) and (np.mod(y, 1) == 0) and 0 < x <= 100 and 0 < y <= 100:
            tokens += (x * 3) + y

    print(tokens)

# print(monotonic() - st)

"""
time: 0.00470458302879706
"""
