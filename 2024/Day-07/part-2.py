import operator  # noqa: INP001, D100
from concurrent.futures import ProcessPoolExecutor
from itertools import product

operator_map = {"+": operator.add, "*": operator.mul, "||": lambda a, b: int(f"{a}{b}")}


def process(line: str) -> int:  # noqa: D103
    value, operands = line.split(":")
    value = int(value)
    operands = list(map(int, operands.strip().split()))
    operators_possibilities = product(operator_map.keys(), repeat=len(operands) - 1)

    for possibility in operators_possibilities:
        total = 0
        for idx, (operand, operation) in enumerate(zip(operands[1:], possibility, strict=False)):
            operator_ = operator_map[operation]
            if not total:
                total = operator_(operands[idx], operand) if operation != "||" else int(operator_(str(operands[idx]), str(operand)))
            else:
                total = operator_(total, operand) if operation != "||" else int(operator_(str(total), str(operand)))

            if total > value:
                break

        if total == value:
            return total
    return 0


def recurse(total: int, value: int, operands: list[int]) -> int:  # noqa: D103
    if total == value and not operands:
        return total

    if total > value or not operands:
        return 0

    for op in operator_map.values():
        if recurse(op(total, operands[0]), value, operands[1:]):
            return value
    return 0


if __name__ == "__main__":
    import time

    s = time.monotonic()
    with open("input.txt") as f:  # noqa: PTH123
        with ProcessPoolExecutor(max_workers=8) as e:
            futures = [e.submit(process, line) for line in f]
            result = [k.result() for k in futures]

        # print(sum(result))  # noqa: T201
    e = time.monotonic()
    # print(" ->", e - s)  # noqa: T201

    s = time.monotonic()
    with open("input.txt") as f, ProcessPoolExecutor(max_workers=8) as executor:  # noqa: PTH123
        futures = []
        for line in f:
            value, operands = line.split(":")
            value = int(value)
            operands = list(map(int, operands.strip().split()))
            futures.append(executor.submit(recurse, operands[0], value, operands[1:]))
        result = [k.result() for k in futures]
        print(sum(result))  # noqa: T201
    e = time.monotonic()
    # print(" ->", e - s)  # noqa: T201

"""
401477450831495
 -> 8.094622067001183
401477450831495
 -> 1.0123130440042587

401477450831495
python part-2.py  21.36s user 0.29s system 605% cpu 3.579 total
"""
