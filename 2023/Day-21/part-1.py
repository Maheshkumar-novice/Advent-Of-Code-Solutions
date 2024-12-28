with open('input.txt', 'r') as f:
    data = []
    for idx, line in enumerate(f):
        line = line.strip()
        if 'S' in line:
            s_index = (idx, line.index('S'))
        data.append(line)
    
    row_length, column_length, next_visits = len(data), len(data[0]), set()
    next_visits.add(s_index)

    for i in range(64):
        visits, next_visits = next_visits, set()

        while visits:
            x, y = visits.pop()

            for dx, dy in ((0, -1), (0, 1), (-1, 0), (1, 0)):
                nx, ny = x + dx, y + dy

                if 0 <= nx < row_length and 0 <= ny < column_length and data[nx][ny] != '#':
                    next_visits.add((nx, ny))

    print(len((next_visits)))
