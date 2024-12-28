from math import prod

with open('input.txt', 'r') as f:
    memory = list(map(int, f.read().split(',')))
    memory[1], memory[2], instruction_pointer = 12, 2, 0

    for address, data in enumerate(memory):
        if address == instruction_pointer and (data == 1 or data == 2):
            operands = (memory[memory[address + 1]],
                        memory[memory[address + 2]])
            memory[memory[address + 3]], instruction_pointer = sum(
                operands) if data == 1 else prod(operands), address + 4

    print(memory[0])
