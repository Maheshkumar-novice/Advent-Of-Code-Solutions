import json


def parse(object: str | int | list | dict) -> None:  # noqa: A002, D103
    total = 0
    if isinstance(object, int):
        total += object
    elif isinstance(object, list):
        for obj in object:
            total += parse(obj)
    elif isinstance(object, dict) and "red" not in object.values():
        for val in object.values():
            total += parse(val)
    return total


with open("input.txt") as f:
    print(parse(json.loads(f.read())))
