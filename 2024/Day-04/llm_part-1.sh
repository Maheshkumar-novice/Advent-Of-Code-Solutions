#!/bin/bash

# Directions: top-left, top, top-right, left, right, bottom-left, bottom, bottom-right
directions=("-1 -1" "-1 0" "-1 1" "0 -1" "0 1" "1 -1" "1 0" "1 1")

count=0
grid=()

# Read grid from input file
readarray -t lines < input.txt
for line in "${lines[@]}"; do
    grid+=("$(echo "$line" | tr -d '\n')")
done

grid_length=${#grid[@]}

# Search for XMAS patterns
for dir in "${directions[@]}"; do
    read -r dx dy <<< "$dir"
    
    for ((row=0; row<grid_length; row++)); do
        for ((col=0; col<grid_length; col++)); do
            # Extract starting character
            text=${grid[row]:col:1}
            
            # Skip if not starting with X
            [[ "$text" != "X" ]] && continue
            
            temp_row=$row
            temp_col=$col
            
            # Try to form XMAS in current direction
            for ((k=0; k<3; k++)); do
                new_row=$((temp_row + dx))
                new_col=$((temp_col + dy))
                
                # Check grid bounds
                if ((new_row >= 0 && new_row < grid_length && 
                     new_col >= 0 && new_col < grid_length)); then
                    text+=${grid[new_row]:new_col:1}
                    temp_row=$new_row
                    temp_col=$new_col
                else
                    break
                fi
            done
            
            # Check if pattern is XMAS
            [[ "$text" == "XMAS" ]] && ((count++))
        done
    done
done

echo "$count"