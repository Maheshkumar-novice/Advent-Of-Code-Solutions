#include <iostream>
#include <fstream>
#include <vector>
#include <string>

int main() {
    std::ifstream input("input.txt");
    std::vector<std::vector<char>> grid_data;
    std::string line;

    // Read grid from file
    while (std::getline(input, line)) {
        std::vector<char> row(line.begin(), line.end());
        grid_data.push_back(row);
    }

    // Directions: top-left, top, top-right, left, right, bottom-left, bottom, bottom-right
    std::vector<std::pair<int, int>> directions = {
        {-1, -1}, {-1, 0}, {-1, 1},
        {0, -1}, {0, 1},
        {1, -1}, {1, 0}, {1, 1}
    };

    int count = 0;
    int grid_length = grid_data.size();
    std::string xmas = "XMAS";

    // Iterate through all directions
    for (const auto& [dx, dy] : directions) {
        // Iterate through all grid positions
        for (int row = 0; row < grid_length; ++row) {
            for (int col = 0; col < grid_length; ++col) {
                // Skip if starting cell is not 'X'
                if (grid_data[row][col] != 'X') continue;

                std::string text(1, grid_data[row][col]);
                int temp_row = row, temp_col = col;

                // Try to form XMAS by moving in current direction
                for (int k = 0; k < 3; ++k) {
                    int new_row = temp_row + dx;
                    int new_col = temp_col + dy;

                    // Check if new position is within grid
                    if (new_row >= 0 && new_row < grid_length && 
                        new_col >= 0 && new_col < grid_length) {
                        text += grid_data[new_row][new_col];
                        temp_row = new_row;
                        temp_col = new_col;
                    } else {
                        break;
                    }
                }

                // Check if formed text is XMAS
                if (text == xmas) {
                    ++count;
                }
            }
        }
    }

    std::cout << count << std::endl;
    return 0;
}