import re

with open("input.txt") as f:
    wire_inputs, gates_logic = f.read().split("\n\n")
    wire_inputs = {e[0]: int(e[1]) for e in re.findall(r"(\w+): (\d+)", wire_inputs)}
    gates_logic = re.findall(r"(\w+) (\w+) (\w+) -> (\w+)", gates_logic)


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
print(int("".join(str(e[1]) for e in sorted([(int(key[1:]), wire_inputs[key]) for key in wire_inputs if key[0] == "z"], key=lambda e: e[0], reverse=True)), 2))
