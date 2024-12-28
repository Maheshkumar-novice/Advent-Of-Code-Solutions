import re
import time

start = time.time()
total = 0

with open('input.txt', 'r') as f:
    for line in f:
        red_max = -1
        blue_max = -1
        green_max = -1

        for result in re.findall(r'(\d+) (?=(red|blue|green))', line):
            if result[1] == 'red':
                if int(result[0]) > red_max:
                    red_max = int(result[0])
            elif result[1] == 'blue':
                if int(result[0]) > blue_max:
                    blue_max = int(result[0])
            elif result[1] == 'green':
                if int(result[0]) > green_max:
                    green_max = int(result[0])


        total += red_max * blue_max * green_max

    print(total)

end = time.time()

print(end - start)
# 0.001008749008178711 s