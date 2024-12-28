def get_count(data):
    for intersection_index in range(1, len(data)):
        taking = data[:intersection_index][::-1]
        remaining = data[intersection_index:]

        diff = 0
        for i, j in (zip(taking, remaining)):
            for char_i, char_j in zip(i, j):
                if char_i != char_j:
                    diff += 1

                if diff > 1:
                    break
            
        if diff == 1:
            return intersection_index


with open('input.txt', 'r') as f:
    total = 0
    for line in f.read().split('\n\n'):
        data = line.split()

        if row_wise := get_count(data):
            total += row_wise * 100

        if column_wise := get_count([*zip(*data)]):
            total += column_wise

      
    print(total)

