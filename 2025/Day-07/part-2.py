# RECURSIVE WRECK
# with open("input.txt") as f:
#     input_data = [list(l) for l in f.read().replace("S", "|").splitlines()]
#     split_count = 0
#     from copy import deepcopy
#     def solve(input_data_copy, index):
#         global split_count
#         if index == len(input_data):
#             return

#         for i, line in enumerate(input_data_copy[index:], index):
#             for j, pos in enumerate(line):
#                 if pos == "." and input_data_copy[i - 1][j] == "|":
#                     if i == len(input_data_copy) - 1:
#                         split_count += 1
#                     input_data_copy[i][j] = "|"

#                 if pos == "^" and input_data_copy[i - 1][j] == "|":
#                     input_data_copy[i][j + 1] = "|"
#                     solve(deepcopy(input_data_copy), i + 1)
#                     input_data_copy[i][j + 1] = "."

#                     input_data_copy[i][j - 1] = "|"
#                     solve(deepcopy(input_data_copy), i + 1)
#                     input_data_copy[i][j - 1] = "."

#     solve(deepcopy(input_data), 1)

#     print(split_count)

with open("input.txt") as f:
    input_data = [list(l) for l in f.read().splitlines()]
    s_r, s_c = [(i, j) for i in range(len(input_data)) for j in range(len(input_data[0])) if input_data[i][j] == "S"][0]

from functools import cache


@cache
def solve(r, c):
    if r == len(input_data):
        return 1

    if input_data[r][c] == "." or input_data[r][c] == "S":
        return solve(r + 1, c)
    if input_data[r][c] == "^":
        return solve(r, c - 1) + solve(r, c + 1)
    return None


print(solve(s_r, s_c), solve.cache_info())

# LEARNED ABOUT scalene profiler - uv add scalene
