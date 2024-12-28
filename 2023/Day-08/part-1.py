import re

with open('input.txt', 'r') as f:
    instruction, _, *nodes = f.read().splitlines()

    network_map = {}

    for data in nodes:
        node, relations = data.split(' = ')
        relations = re.findall(r'\w+', relations)

        network_map[node] = relations

    loop_index = 0
    steps = 0
    loop_max = len(instruction)
    node = 'AAA'

    while True:
        if loop_index >= loop_max:
            loop_index = 0

        if instruction[loop_index] == 'R':
            node = network_map[node][1]
        else:
            node = network_map[node][0]

        steps += 1
        if node == 'ZZZ':
            break

        loop_index += 1
    print(steps)