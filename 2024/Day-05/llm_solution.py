def parse_input(input_str):
    """
    Parse the input string into two parts:
    1. Ordering rules (which pages must come before others)
    2. Update sequences to check
    """
    # Split the input into lines
    lines = input_str.strip().split('\n')
    
    # Find the first empty line to separate rules from updates
    separator_index = lines.index('')
    
    # Parse ordering rules
    rules = {}
    for rule in lines[:separator_index]:
        before, after = map(int, rule.split('|'))
        if before not in rules:
            rules[before] = set()
        if after not in rules:
            rules[after] = set()
        rules[before].add(after)
    
    # Parse update sequences
    updates = [list(map(int, update.split(','))) for update in lines[separator_index+1:]]
    
    return rules, updates

def is_update_valid(update, rules):
    """
    Check if an update is in a valid order according to the rules.
    """
    applicable_rules = {}
    for page in update:
        applicable_rules[page] = set()
    
    for before, afters in rules.items():
        if before in update and any(after in update for after in afters):
            applicable_rules[before].update(
                after for after in afters if after in update
            )
    
    for i, page in enumerate(update):
        for forbidden_after in applicable_rules[page]:
            if update.index(forbidden_after) < i:
                return False
    
    return True

def correct_update_order(update, rules):
    """
    Correctly order an update according to the rules.
    Uses a topological sorting approach.
    """
    graph = {page: set() for page in update}
    in_degree = {page: 0 for page in update}
    
    for before, afters in rules.items():
        if before in update:
            for after in afters:
                if after in update and after not in graph[before]:
                    graph[before].add(after)
                    in_degree[after] += 1
    
    import heapq
    queue = [page for page in update if in_degree[page] == 0]
    heapq.heapify(queue)
    
    result = []
    while queue:
        page = heapq.heappop(queue)
        result.append(page)
        
        for next_page in graph[page]:
            in_degree[next_page] -= 1
            if in_degree[next_page] == 0:
                heapq.heappush(queue, next_page)
    
    return result

def solve_page_order_problem(input_str):
    """
    Solve both parts of the problem.
    Returns a tuple with Part One and Part Two results.
    """
    # Parse input into rules and updates
    rules, updates = parse_input(input_str)
    
    # Part One: Valid updates
    valid_middle_pages = []
    for update in updates:
        if is_update_valid(update, rules):
            middle_index = len(update) // 2
            valid_middle_pages.append(update[middle_index])
    
    # Part Two: Incorrectly ordered updates
    incorrect_middle_pages = []
    for update in updates:
        if not is_update_valid(update, rules):
            corrected_update = correct_update_order(update, rules)
            middle_index = len(corrected_update) // 2
            incorrect_middle_pages.append(corrected_update[middle_index])
    
    return sum(valid_middle_pages), sum(incorrect_middle_pages)

# Read input from file
with open('input.txt', 'r') as file:
    puzzle_input = file.read()

# Solve the puzzle
part_one, part_two = solve_page_order_problem(puzzle_input)
print(f"Part One: {part_one}")
print(f"Part Two: {part_two}")
