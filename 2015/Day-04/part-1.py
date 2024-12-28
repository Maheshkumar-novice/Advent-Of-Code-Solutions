import hashlib

with open("input.txt") as f:
    input_data = f.read().strip().encode()
    for i in range(1, 10000000):
        if hashlib.md5(input_data + str(i).encode()).hexdigest().startswith("00000"):  # noqa: S324
            print(i)
            break
