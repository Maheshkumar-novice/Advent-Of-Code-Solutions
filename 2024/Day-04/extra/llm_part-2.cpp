#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <array>

int main() {
    std::ifstream input("input.txt");
    std::vector<std::vector<char>> grid_data;
    std::string line;

    // Read grid from file
    while (std::getline(input, line)) {
        std::vector<char> row(line.begin(), line.end());
        grid_data.push_back(row);
    }

    // Directions: top-left, top-right, bottom-left, bottom-right
    std::vector<std::pair<int, int>> directions = {
        {-1, -1}, {-1, 1},
        {1, -1}, {1, 1}
    };

    std::vector<std::string> allowed_val = {"M", "S"};
    std::array<std::string, 4> values = {"1", "2", "3", "4"};

    int count = 0;
    int grid_length = grid_data.size();

    // Iterate through grid
    for (int row = 0; row < grid_length; ++row) {
        for (int col = 0; col < grid_length; ++col) {
            // Skip if starting cell is not 'A'
            if (grid_data[row][col] != 'A') continue;

            int updates = 0;
            values = {"1", "2", "3", "4"};  // Reset values for each 'A'

            for (int idx = 0; idx < directions.size(); ++idx) {
                auto [dx, dy] = directions[idx];
                int new_row = row + dx;
                int new_col = col + dy;

                // Check if new position is valid and contains allowed value
                if (new_row >= 0 && new_row < grid_length && 
                    new_col >= 0 && new_col < grid_length) {
                    for (const auto& val : allowed_val) {
                        if (grid_data[new_row][new_col] == val[0]) {
                            values[idx] = val;
                            ++updates;
                            break;
                        }
                    }
                }
            }

            // Check pattern conditions
            if (updates == 4 && values[0] != values[3] && values[1] != values[2]) {
                ++count;
            }
        }
    }

    std::cout << count << std::endl;
    return 0;
}