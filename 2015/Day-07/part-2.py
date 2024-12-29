import re


def _get_input_value(input_: str) -> int | None:
    if input_.isnumeric():
        return int(input_)
    if input_ in wire_values:
        return int(wire_values[input_])
    return None


with open("input.txt") as f:
    input_data = f.read().splitlines()

pattern = re.compile(r"(.+) -> (\w+)")
wire_values, instructions = {}, []

for logic in input_data:
    input_logic, output_wire = pattern.match(logic).groups()
    instructions.append((input_logic, output_wire))

operations = {
    "AND": lambda x, y: x & y,
    "OR": lambda x, y: x | y,
    "LSHIFT": lambda x, y: x << y,
    "RSHIFT": lambda x, y: x >> y,
    "NOT": lambda x: x ^ 65535,
}

while True:
    remaining = []
    for input_logic, output_wire in instructions:
        match input_logic.split():
            case [input_1, operation, input_2]:
                input_1 = _get_input_value(input_1)
                input_2 = _get_input_value(input_2)

                if input_1 is not None and input_2 is not None:
                    wire_values[output_wire] = operations[operation](input_1, input_2)
                else:
                    remaining.append((input_logic, output_wire))
            case [operation, input_]:
                input_ = _get_input_value(input_)

                if input_ is not None:
                    wire_values[output_wire] = operations[operation](input_)
                else:
                    remaining.append((input_logic, output_wire))
            case [input_]:
                input_ = _get_input_value(input_)

                if output_wire == "b":
                    input_ = 16076

                if input_ is not None:
                    wire_values[output_wire] = input_
                else:
                    remaining.append((input_logic, output_wire))
    if not remaining:
        break
    instructions = remaining
print(wire_values["a"])
