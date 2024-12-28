with open('input.txt', 'r') as f:
    point, previous_point, shoelace, length = [0, -1], [0, 0], 0, 0

    for line in f:
        _, _, instruction = line.split()
        steps = int(instruction[2:7], 16)

        match int(instruction[-2]):
            case 0:
                point[1] += steps
            case 2:
                point[1] -= steps
            case 3:
                point[0] -= steps
            case 1:
                point[0] += steps

        shoelace += ((point[0] * previous_point[1]) - (point[1] * previous_point[0]))
   
        previous_point = point.copy()
        length += steps

    print(abs(shoelace) // 2 + length // 2 + 1)
