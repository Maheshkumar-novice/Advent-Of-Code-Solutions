# Claude.AI
def solve_day1(file_path):
    # Read the input file
    with open(file_path) as f:
        lines = f.readlines()

    # Parse the lines into left and right lists
    left_list = []
    right_list = []
    for line in lines:
        left, right = map(int, line.strip().split())
        left_list.append(left)
        right_list.append(right)

    # Part 1: Calculate total distance
    left_sorted = sorted(left_list)
    right_sorted = sorted(right_list)

    total_distance = sum(abs(left - right) for left, right in zip(left_sorted, right_sorted))
    print(f"Part 1 - Total Distance: {total_distance}")

    # Part 2: Calculate similarity score
    right_count = {}
    for num in right_list:
        right_count[num] = right_count.get(num, 0) + 1

    similarity_score = sum(num * right_count.get(num, 0) for num in left_list)
    print(f"Part 2 - Similarity Score: {similarity_score}")

    return total_distance, similarity_score


# Run the solution
file_path = "input.txt"
solve_day1(file_path)
