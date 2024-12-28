with open("input.txt") as f:
    sum_ = 0
    for idx, char in enumerate(f.read()):
        sum_ += -1 if char == ")" else 1

        if sum_ == -1:
            print(idx + 1)
            break
