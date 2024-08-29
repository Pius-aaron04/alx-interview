""" 0-island_perimeter.py

Contains a function
"""


def island_perimeter(grid):
    """
    Calculate the perimeter of the island described in grid.

    Args:
        grid: List[List[int]] list of list of int - 2D grid map of 0s and 1s.

    Return:
        int: perimeter of the island.
    """

    if not grid:
        return 0

    rows, cols = len(grid), len(grid[0])
    perimeter = 0

    # use nested loop to iterate through each cell in grid
    for r in range(rows):
        for c in range(cols):
            # check for each cell if it contains land
            if grid[r][c] == 1:  # land cell
                # check all 4 directions (up, down, left, right) for water
                # if water is found, increment perimeter by 1
                if r == 0 or grid[r - 1][c] == 0:  # check cells above
                    perimeter += 1
                if r == rows - 1 or grid[r + 1][c] == 0:  # check cells below
                    perimeter += 1
                if c == 0 or grid[r][c - 1] == 0:  # check cells to the left
                    perimeter += 1
                # check cells to the right
                if c == cols - 1 or grid[r][c + 1] == 0:
                    perimeter += 1

    return perimeter
