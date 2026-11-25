# https://adventofcode.com/2022/day/1

# Input:
# File with the numbers
# numbers represent the calories held by the Elves
# each of the elves may have multiple items so all the calories
# listed one by one
# To separate one Elf's calorie with another blank line is used.

# Output:
# Calories of the Elf who contains the most Calories

# Thoughts:
# We have the calories separated by blank lines. 
# So we can go through the calories one by one and we add it to 
# the temporary variable or something
# then when we encounter a blank line we need to compare the 
# value with the max and update the max if needed
# Continue this until we reach the end of the file.
# This way we go through each line of the file and we can find the value
# we need.

# Process:
# Set max as 0, elf_calories as 0
# Go through each line of the file
#   If the line is not blank
#       Add the value to elf_calories
#   else
#       If the elf_calories > max
#           Update max with elf_calories
#           Set elf_calories as 0
# Print the max value

max_calories = 0
elf_calories = 0

with open('input.txt', 'r') as file:
    for line in file:
        calorie_value = line.rstrip()

        if calorie_value:
            elf_calories += int(calorie_value)
        else:
            if elf_calories > max_calories:
                max_calories = elf_calories

            elf_calories = 0

print(f'Max Calories: {max_calories}')

