#!/bin/bash

# Read grid from input file
mapfile -t grid < input.txt

# Get grid dimensions
grid_length=${#grid[@]}

# Directions: top-left, top-right, bottom-left, bottom-right
directions=("$((0-1)) $((0-1))" "$((0-1)) 1" "1 $((0-1))" "1 1")

# Allowed values
allowed_val=("M" "S")

count=0

# Iterate through grid
for ((row=0; row<grid_length; row++)); do
    for ((col=0; col<grid_length; col++)); do
        # Skip if starting cell is not 'A'
        [[ "${grid[row]:col:1}" != "A" ]] && continue

        # Reset values and updates for each 'A'
        values=("1" "2" "3" "4")
        updates=0

        # Check adjacent cells in four diagonal directions
        for idx in "${!directions[@]}"; do
            read -r dx dy <<< "${directions[idx]}"
            new_row=$((row + dx))
            new_col=$((col + dy))

            # Check grid bounds
            if ((new_row >= 0 && new_row < grid_length && 
                 new_col >= 0 && new_col < grid_length)); then
                adj_char="${grid[new_row]:new_col:1}"

                # Check if adjacent cell matches allowed values
                for val in "${allowed_val[@]}"; do
                    if [[ "$adj_char" == "$val" ]]; then
                        values[idx]="$val"
                        ((updates++))
                        break
                    fi
                done
            fi
        done

        # Check pattern conditions
        if ((updates == 4)) && 
           [[ "${values[0]}" != "${values[3]}" ]] && 
           [[ "${values[1]}" != "${values[2]}" ]]; then
            ((count++))
        fi
    done
done

echo "$count"