import re
import time

start = time.time()

total = 0
with open('input.txt', 'r') as f:
    for line in f:
        red   = max(int(i) for i in re.findall(r'\d+ (?=red)', line))
        blue  = max(int(i) for i in re.findall(r'\d+ (?=blue)', line))
        green = max(int(i) for i in re.findall(r'\d+ (?=green)', line))

        total += red * blue * green

    print(total)

end = time.time()

print(end-start)
# 0.001294851303100586 s