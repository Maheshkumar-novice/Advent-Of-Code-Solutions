from itertools import product
from math import prod

with open('input.txt', 'r') as f:
    MEMORY = list(map(int, f.read().split(',')))

    for noun, verb in product(range(0, 100), repeat=2):
        memory = MEMORY.copy()
        memory[1], memory[2], instruction_pointer = noun, verb, 0

        for address, data in enumerate(memory):
            if address == instruction_pointer and (data == 1 or data == 2):
                operands = (memory[memory[address + 1]],
                            memory[memory[address + 2]])
                memory[memory[address + 3]], instruction_pointer = sum(
                    operands) if data == 1 else prod(operands), address + 4

        if memory[0] == 19690720:
            print(100 * noun + verb)
            break
