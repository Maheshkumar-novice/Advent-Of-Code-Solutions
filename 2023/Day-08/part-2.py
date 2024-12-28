import re
from math import lcm

with open('input.txt', 'r') as f:
    instruction, _, *nodes = f.read().splitlines()

    network_map = {}
    nodes_of_navigation = []

    for data in nodes:
        node, relations = data.split(' = ')
        relations = re.findall(r'\w+', relations)

        if node.endswith('A'):
            nodes_of_navigation.append(node)

        network_map[node] = relations

    
    loop_max = len(instruction)
    navigation_results = []

    for node in nodes_of_navigation:
        loop_index = 0
        steps = 0
        while True:
            if loop_index >= loop_max:
                loop_index = 0
            
            if instruction[loop_index] == 'R':
                node = network_map[node][1]
            else:
                node = network_map[node][0]

            steps += 1
            if node.endswith('Z'):
                navigation_results.append(steps)
                break

            loop_index += 1
    

    print(lcm(*navigation_results))