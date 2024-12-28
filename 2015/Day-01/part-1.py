with open("input.txt") as f:
    print(sum(1 if c == "(" else -1 for c in f.read()))
