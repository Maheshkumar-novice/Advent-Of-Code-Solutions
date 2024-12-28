def get_count(data):
    for intersection_index in range(1, len(data)):
        taking = data[:intersection_index][::-1]
        remaining = data[intersection_index:]

        if all(i == j for i, j in (zip(taking, remaining))):
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

