with open('input.txt', 'r') as f:
    f = f.read().splitlines()
    total = 1
    for time, distance in zip(map(int, f[0].split()[1::]), map(int, f[1].split()[1::])):
        holding_time, record_breaking_count = 0, 0
        while time > 0:
            if holding_time * time > distance:
                record_breaking_count += 1
            holding_time += 1
            time -= 1

        if record_breaking_count:
            total *= record_breaking_count
    print(total)
