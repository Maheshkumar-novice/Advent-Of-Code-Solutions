# PART 2 DOESN'T WORK. MAYBE I NEED TO UPDATE THE PROMPT OR GIVE MORE CONTEXT.
def count_xmas(grid):
    """Count XMAS occurrences (Part 1)"""
    rows, cols = len(grid), len(grid[0])
    xmas_count = 0
    
    directions = [
        (0, 1), (0, -1), (1, 0), (-1, 0),
        (1, 1), (1, -1), (-1, 1), (-1, -1)
    ]
    
    def is_valid(r, c):
        return 0 <= r < rows and 0 <= c < cols
    
    def check_word(r, c, dr, dc):
        target = "XMAS"
        for i, letter in enumerate(target):
            curr_r, curr_c = r + i * dr, c + i * dc
            if not is_valid(curr_r, curr_c) or grid[curr_r][curr_c] != letter:
                return False
        return True
    
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 'X':
                for dr, dc in directions:
                    if check_word(r, c, dr, dc):
                        xmas_count += 1
    
    return xmas_count
def count_x_mas(grid):
    """Count X-MAS occurrences (Part 2)"""
    rows, cols = len(grid), len(grid[0])
    x_mas_count = 0
    
    def check_mas(r, c, dr, dc):
        """Check forward and backward MAS patterns"""
        # Forward MAS: M-A-S
        if (0 <= r + 2*dr < rows and 0 <= c + 2*dc < cols):
            if (grid[r][c] == 'M' and 
                grid[r + dr][c + dc] == 'A' and 
                grid[r + 2*dr][c + 2*dc] == 'S'):
                return True
        
        # Backward MAS: S-A-M
        if (0 <= r + 2*dr < rows and 0 <= c + 2*dc < cols):
            if (grid[r][c] == 'S' and 
                grid[r + dr][c + dc] == 'A' and 
                grid[r + 2*dr][c + 2*dc] == 'M'):
                return True
        
        return False
    
    # Iterate through potential X centers
    for r in range(rows):
        for c in range(cols):
            # Check all possible X configurations
            x_configs = [
                # Upward-right and downward-left diagonals
                ((1, 1), (-1, -1)),   # Down-right and Up-left
                ((1, -1), (-1, 1)),   # Down-left and Up-right
            ]
            
            for (dr1, dc1), (dr2, dc2) in x_configs:
                # Check if both diagonals have valid MAS patterns
                if (check_mas(r, c, dr1, dc1) and 
                    check_mas(r, c, dr2, dc2)):
                    x_mas_count += 1
    
    return x_mas_count

# Read input from file
with open('input.txt', 'r') as file:
    word_search = [line.strip() for line in file]

# Solve and print results for both parts
part1_result = count_xmas(word_search)
part2_result = count_x_mas(word_search)

print(f"Part 1 - Number of XMAS occurrences: {part1_result}")
print(f"Part 2 - Number of X-MAS occurrences: {part2_result}")