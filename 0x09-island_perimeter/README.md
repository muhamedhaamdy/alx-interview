# 0x09. Island Perimeter

## Description

This project focuses on solving the "Island Perimeter" problem. The objective is to determine the perimeter of an island represented in a 2D grid, where `0` represents water and `1` represents land.

## Problem Statement

You are given a 2D grid map where:

- `0` represents water
- `1` represents land

The grid is surrounded entirely by water, and there is exactly one island (or one or more connected land cells).


## Implementation

Below is a Python implementation of the solution:

```python
def island_perimeter(grid):
    """
    Calculates the perimeter of the island in the given grid.

    :param grid: List of List of integers, where 0 represents water and 1 represents land
    :return: Integer representing the perimeter of the island
    """
    if not grid or not grid[0]:
        return 0
    
    perimeter = 0
    rows, cols = len(grid), len(grid[0])
    
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                # Add 4 for each land cell
                perimeter += 4
                # Subtract 2 for each adjacent land cell
                if i > 0 and grid[i-1][j] == 1:  # Check the cell above
                    perimeter -= 2
                if j > 0 and grid[i][j-1] == 1:  # Check the cell to the left
                    perimeter -= 2
    
    return perimeter

# Example usage
if __name__ == "__main__":
    grid = [
        [0, 1, 0, 0],
        [1, 1, 1, 0],
        [0, 1, 0, 0],
        [0, 1, 0, 0]
    ]
    print(island_perimeter(grid))  # Output: 16
