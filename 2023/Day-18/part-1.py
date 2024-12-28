with open('input.txt', 'r') as f:
    point, previous_point, shoelace, length = [0, -1], [0, 0], 0, 0
    
    for line in f:
        direction, steps, _ = line.split()
        steps = int(steps)

        match direction:
            case 'R':
                point[1] += steps
            case 'L':
                point[1] -= steps
            case 'U':
                point[0] -= steps
            case 'D':
                point[0] += steps
        
        shoelace += ((point[0] * previous_point[1]) - (point[1] * previous_point[0]))
        
        previous_point = point.copy()
        length += steps      

    print(abs(shoelace) // 2 + length // 2  + 1)
