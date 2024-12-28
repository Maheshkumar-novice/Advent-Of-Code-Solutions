from heapq import heappop, heappush

with open('input.txt', 'r') as f:
    data = f.read().splitlines()
    maze = [list(map(int, list(i))) for i in data]


row_length = len(maze)
column_length = len(maze[0])
visited = set()
queue = [(0, 0, 0, -1, 0)]

while queue:
    h, x, y, d, s = heappop(queue)

    if (x, y, d, s) in visited:
        continue

    visited.add((x, y, d, s))

    if (x == row_length -1 and y == column_length - 1) and s >= 4:
        print(h)
        break

    for i, (dx, dy) in enumerate([(0, -1), (1, 0), (0, 1), (-1, 0)]):
        nx, ny = x + dx, y + dy
        if 0 <= nx < row_length and 0 <= ny < column_length:
            if d == i and s < 10 or d == -1:
                heappush(queue, (h + maze[nx][ny], nx, ny, i, s + 1))
            elif i % 2 != d % 2 and (s >= 4):
                heappush(queue, (h + maze[nx][ny], nx, ny, i, 1))
