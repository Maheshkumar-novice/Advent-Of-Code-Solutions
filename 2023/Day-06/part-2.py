with open('input.txt', 'r') as f:
    f = f.read().splitlines()
    time = int(''.join(f[0].split()[1::]))
    distance = int(''.join(f[1].split()[1::]))
    total = 1
    holding_time, record_breaking_count = 0, 0
    while holding_time < time:
        if holding_time * time > distance:
            record_breaking_count += 1
        holding_time += 1
        time -= 1

    if record_breaking_count:
        total *= record_breaking_count
    print(total * 2)
