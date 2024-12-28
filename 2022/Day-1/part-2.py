# https://adventofcode.com/2022/day/1

# Input:
# File with the numbers
# numbers represent the calories held by the Elves
# each of the elves may have multiple items so all the calories
# listed one by one
# To separate one Elf's calorie with another blank line is used.

# Output:
# Total Calories of the 3 elves who have the most calories.

# Thoughts:
# For the single max we just used a variable to compare and swap the max value
# accordinly.
# Here we need to find the top 3 not just top 1.
# How we can approach this? 
# Questions:
# * How an elf's calories enter the top 3?
#       Whenever the elf's calories is greater than the least of the top 3 elves calories.
# After entering the top 3 positions how the elf gets it's place 3 or 2 or 1?
# (3rd highest calorie) < (2nd highest calorie) < (1st highest calorie)
# So an elf gets qualified for the top3 whenever it's calories is > than the 3rd highest one.
# If the calorie is > than the 3rd one and lesser than the 2nd one,
#   (new_value) < (2nd) < (1st)
# If the calorie is > than the 3rd & 2nd but lesser than the 1st one,
#   (2nd) < (new_value) < (1st)
# If the calorie is > than all 3 values then,
#   (2nd) < (1st) < (new_value)
# Now we need to sum and return these top 3.
# Now the question is how we can represent and achieve this top 3 whenever we get an elf's calorie?
# We need to represent in such a way that we can even extend this to multiple values. Is it possible?
# We can write the simple condition solution for it. But if we get a requirement like top 4 we should 
# update the code again.
# Let's think of an extensible solution after coding the conditional solution first.

# Process:
# set a hash structure to store top 3 calories 1st, 2nd, 3rd - default value with -1
# set elf_calories = 0
# for each line of the file:
#   if this is a line break?
#       if elf_calories > 3rd but < 2nd:
#           set elf_calories as 3rd
#       else if elf_calories > 3rd and > 2nd but < 1st:
#           set elf_calories as 2nd
#           set 2nd as 3rd
#       else
#           set elf_calories as 1st
#           set 1st as 2nd
#           set 2nd as 3rd
#       reset elf_calories
#   else
#       add the value to elf_calories

top_3_calories = {'1st': -1, '2nd': -1, '3rd': -1}
elf_calories = 0

with open('input.txt', 'r') as file:
    for line in file:
        value = line.rstrip()
        if not value:
            if elf_calories > top_3_calories['3rd'] and elf_calories < top_3_calories['2nd']:
                top_3_calories['3rd'] = elf_calories
            elif elf_calories > top_3_calories['3rd'] and elf_calories > top_3_calories['2nd'] and elf_calories < top_3_calories['1st']:
                top_3_calories['3rd'] = top_3_calories['2nd']
                top_3_calories['2nd'] = elf_calories
            elif elf_calories > top_3_calories['3rd'] and elf_calories > top_3_calories['2nd'] and elf_calories > top_3_calories['1st']:
                top_3_calories['3rd'] = top_3_calories['2nd']
                top_3_calories['2nd'] = top_3_calories['1st']
                top_3_calories['1st'] = elf_calories
            elf_calories = 0
            # print(top_3_calories)
        else:
            elf_calories += int(value)

print(f'Sum of Top 3 Calories {top_3_calories.values()}: {sum(top_3_calories.values())}')
