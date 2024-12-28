import re


def parse_corrupted_memory(memory, part=1):
    # Regex patterns
    mul_pattern = r"mul\((\d{1,3})\s*,\s*(\d{1,3})\)"
    do_pattern = r"do\(\)"
    dont_pattern = r"don\'t\(\)"

    # Track multiplication status (only for part 2)
    mul_enabled = True if part == 2 else None
    total_sum = 0

    # Scan for all relevant instructions
    if part == 1:
        # Simple pattern for part 1
        matches = re.findall(mul_pattern, memory)
        total_sum = sum(int(x) * int(y) for x, y in matches)
    else:
        # More complex parsing for part 2
        tokens = re.findall(r"(?:mul\(\d{1,3}\s*,\s*\d{1,3}\))|(?:do\(\))|(?:don\'t\(\))", memory)

        for token in tokens:
            # Check for do/don't instructions first
            if re.match(do_pattern, token):
                mul_enabled = True
            elif re.match(dont_pattern, token):
                mul_enabled = False

            # Process mul instructions if enabled
            elif re.match(mul_pattern, token):
                if mul_enabled:
                    match = re.match(mul_pattern, token)
                    x, y = map(int, match.groups())
                    total_sum += x * y

    return total_sum


# Solve the puzzle
def solve_puzzle(part):
    with open("input.txt", "r") as file:
        puzzle_input = file.read().strip()
        return parse_corrupted_memory(puzzle_input, part)


# Run the solution
if __name__ == "__main__":
    print(f"Part 1 solution: {solve_puzzle(1)}")
    print(f"Part 2 solution: {solve_puzzle(2)}")
