import operator
import re

with open('input.txt', 'r') as f:
    operator_map, instructions, total = {'>': operator.gt, '<': operator.lt}, {}, 0

    def exec_instruction(instruction='in'):
        if instruction in 'RA':
            return 'RA'.index(instruction)

        steps = iter(instructions[instruction])
        while True:
            match next(steps).split(':'):
                case [condition, next_instruction]:
                    if operator_map[condition[1]](line_val_map[condition[0]], int(condition[2:])):
                        return exec_instruction(next_instruction)
                case [next_instruction]:
                    return exec_instruction(next_instruction)

    for line in f:
        if line == '\n':
            break

        key, instruction, *_  = re.match(r'(\w+){((\w+[><]\d+:\w+,)+(\w+))}', line).groups()
        instructions[key] = instruction.split(',')

    for line in f:
        line, line_val_map = line.strip()[1:-1].split(','), {}
        for val in line:
            a, b = val.split('=')
            line_val_map[a] = int(b)

        if exec_instruction():
            total += sum(line_val_map.values())

    print(total)
