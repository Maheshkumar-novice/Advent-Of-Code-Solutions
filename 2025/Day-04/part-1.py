with open("input.txt") as f:
    data = [list(line.strip()) for line in f]
    result = 0
    for i in range(len(data)):
        for j in range(len(data[0])):
            if data[i][j] != "@":
                continue
            count = 0
            for dx, dy in [(-1, -1), (-1, 0), (-1, 1), (1, -1), (1, 0), (1, 1), (0, -1), (0, 1)]:
                x, y = i + dx, j + dy
                if 0 <= x < len(data) and 0 <= y < len(data[0]) and data[x][y] == "@":
                    count += 1
            if count < 4:
                result += 1
    print(result)
