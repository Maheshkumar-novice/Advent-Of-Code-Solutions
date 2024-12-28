import re
from math import prod


def exec_workflow(xmas_range_map, workflow, total=0): 
        workflow = workflow[::-1]

        match workflow:
            case ['A']:
                return prod((xmas_val[-1] - xmas_val[0]) + 1 for xmas_val in xmas_range_map.values())
            case ['R']:
                return 0

        match workflow.pop().split(':'):
            case [condition, next_workflow]:
                operator, xmas_val, value = condition[1], condition[0], int(condition[2:])
                range = xmas_range_map[xmas_val]

                if operator == '<':
                    split_1_map = xmas_range_map.copy()
                    split_1_map[xmas_val] = (range[0], value - 1)
                    total += exec_workflow(split_1_map, workflows[next_workflow])

                    split_2_map = xmas_range_map.copy()
                    split_2_map[xmas_val] = (value, range[-1])
                    total += exec_workflow(split_2_map, workflow[::-1])
                if operator == '>':
                    split_1_map = xmas_range_map.copy()
                    split_1_map[xmas_val] = (value + 1, range[-1])
                    total += exec_workflow(split_1_map, workflows[next_workflow])

                    split_2_map = xmas_range_map.copy()
                    split_2_map[xmas_val] = (range[0], value)
                    total += exec_workflow(split_2_map, workflow[::-1])
            case [next_workflow]:
                total += exec_workflow(xmas_range_map, workflows[next_workflow])

        return total

with open('input.txt', 'r') as f:
    workflows = {'R': ['R'], 'A': ['A']}

    for line in f:
        if line == '\n':
            break

        key, workflow, *_  = re.match(r'(\w+){((\w+[><]\d+:\w+,)+(\w+))}', line).groups()
        workflows[key] = workflow.split(',')

    print(exec_workflow({i: (1, 4000) for i in 'xmas'}, workflows['in']))
