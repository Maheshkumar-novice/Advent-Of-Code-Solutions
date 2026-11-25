def is_report_safe(levels, allow_single_removal=False):
    def check_levels(check_levels):
        # Check if levels are strictly increasing or decreasing
        increasing = all(check_levels[i] < check_levels[i + 1] for i in range(len(check_levels) - 1))
        decreasing = all(check_levels[i] > check_levels[i + 1] for i in range(len(check_levels) - 1))

        # Check if adjacent levels differ by at least 1 and at most 3
        level_diffs_valid = all(1 <= abs(check_levels[i] - check_levels[i + 1]) <= 3 for i in range(len(check_levels) - 1))

        return (increasing or decreasing) and level_diffs_valid

    # First, check if report is already safe
    if check_levels(levels):
        return True

    # If removal is not allowed, return False
    if not allow_single_removal:
        return False

    # Try removing each level to see if it becomes safe
    for i in range(len(levels)):
        # Create a new list without the current level
        modified_levels = levels[:i] + levels[i + 1 :]

        # Check if modified report is safe
        if check_levels(modified_levels):
            return True

    return False


def solve_puzzle(filename, part2=False):
    with open(filename, "r") as file:
        reports = [[int(level) for level in line.strip().split()] for line in file]

    return sum(1 for report in reports if is_report_safe(report, allow_single_removal=part2))


# Solve Part 1
print("Part 1:", solve_puzzle("input.txt", part2=False))

# Solve Part 2
print("Part 2:", solve_puzzle("input.txt", part2=True))
