#!/usr/bin/python3
''' calculates the perimeter of an island '''


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
