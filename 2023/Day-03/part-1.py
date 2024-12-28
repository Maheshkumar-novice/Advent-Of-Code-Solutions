def fill_adjacent_indices(row, column, adjacent_indices):
    # TOP
    if row - 1 >= 0:
        adjacent_indices.append([row - 1, column])
    
    # BOTTOM
    adjacent_indices.append([row + 1, column])

    # LEFT
    if column - 1 >= 0:
        adjacent_indices.append([row, column - 1])

    # RIGHT
    adjacent_indices.append([row, column + 1])

    # TR_DIAG - row -1, column + 1
    if row - 1 >= 0:
        adjacent_indices.append([row - 1, column + 1])

    # TL_DIAG - row - 1, column - 1
    if row - 1 >= 0:
        adjacent_indices.append([row - 1, column - 1])

    # BR_DIAG - row + 1, column + 1
    adjacent_indices.append([row + 1, column + 1])

    # BL_DIAG - row + 1, column - 1
    if column - 1 >= 0:
        adjacent_indices.append([row + 1, column - 1])

    return adjacent_indices


def adjacent_indices_have_symbol(adjacent_indices, array):
    for row, column in adjacent_indices:
        try:
            if array[row][column] != '.' and not array[row][column].isdigit():
                return True
        except Exception:
            ...
    return False
    


with open('input.txt', 'r') as f:
    array = []
    for line in f:
        array.append(list(line.strip()))

    total = 0
    number = ''
    adjacent_indices = []

    for row, line in enumerate(array):
        for column, char in enumerate(line):
            if char.isdigit():
                number += char
                fill_adjacent_indices(row, column, adjacent_indices)
            else:
                if adjacent_indices_have_symbol(adjacent_indices, array):
                    total += int(number)
                number = ''
                adjacent_indices = []
    print(total)
