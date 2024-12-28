"""Manual effort using the visual representation. I LOVED THIS PUZZLE!."""

import re

from graphviz import Digraph

with open("input.txt") as f:
    wire_inputs, gates_logic = f.read().split("\n\n")
    wire_inputs = {e[0]: int(e[1]) for e in re.findall(r"(\w+): (\d+)", wire_inputs)}
    gates_logic = re.findall(r"(\w+) (\w+) (\w+) -> (\w+)", gates_logic)


d = Digraph("Gate", graph_attr={"size": "500,500", "dpi": "100"})

for k in wire_inputs:
    d.node(k, k)


for a, b, c, de in gates_logic:
    d.node(f"{a}{c}{b}", b)
    d.edge(a, f"{a}{c}{b}")
    d.edge(c, f"{a}{c}{b}")
    d.edge(f"{a}{c}{b}", de)

d.render("final", format="pdf", cleanup=True)


while True:
    remaining = []
    for ip_wire_1, gate_type, ip_wire_2, op_wire in gates_logic:
        if ip_wire_1 in wire_inputs and ip_wire_2 in wire_inputs:
            ip_wire_1 = wire_inputs[ip_wire_1]  # noqa: PLW2901
            ip_wire_2 = wire_inputs[ip_wire_2]  # noqa: PLW2901
            if gate_type == "AND":
                output = int(ip_wire_1 and ip_wire_2)
            elif gate_type == "OR":
                output = int(ip_wire_1 or ip_wire_2)
            elif gate_type == "XOR":
                output = int(ip_wire_1 != ip_wire_2)
            wire_inputs[op_wire] = output
        else:
            remaining.append((ip_wire_1, ip_wire_2, gate_type, op_wire))

    if not remaining:
        break

# This is too much for a single line! But why not? lol :)
x_sum = int("".join(str(e[1]) for e in sorted([(int(key[1:]), wire_inputs[key]) for key in wire_inputs if key[0] == "x"], key=lambda e: e[0], reverse=True)), 2)
y_sum = int("".join(str(e[1]) for e in sorted([(int(key[1:]), wire_inputs[key]) for key in wire_inputs if key[0] == "y"], key=lambda e: e[0], reverse=True)), 2)
z_sum = int("".join(str(e[1]) for e in sorted([(int(key[1:]), wire_inputs[key]) for key in wire_inputs if key[0] == "z"], key=lambda e: e[0], reverse=True)), 2)
# print(x_sum)
# print(y_sum)
# print(z_sum)
print("Addition Successful!" if x_sum + y_sum == z_sum else ":(")
# Swapped Wires: rpp,z39,z23,kdf,fdv,dbp,z15,ckj
# I've used graphviz to visualize this ripple carry adder (I guess). During the investigation I found out the swapped
# wires. Then I fixed those wires and when I saw the output, the difference got reduced.
# I looked for the mismatch in the structure of the adder. Here we see that z* wire is always come out of XOR gate.
# That helped me find out 3 swapped wires. Other caught in my eye because in the graph that one alone had a XOR-AND swapped.
