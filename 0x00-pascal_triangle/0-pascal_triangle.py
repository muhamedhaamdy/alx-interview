#!/usr/bin/python3

'''
this function return 2d list that contains pascal's triangle
'''


def pascal_triangle(n):
    """Create a function def pascal_triangle(n): that returns a list of lists
    of integers representing the Pascal’s triangle of n
    """
    c = [[0] * (i + 1) for i in range(n)]
    for row in range(5):
        for col in range(row + 1):
            if not row and not col:
                c[row][col] = 1
            elif col == 0 or col == row:
                c[row][col] = 1
            else:
                c[row][col] = c[row - 1][col - 1] + c[row - 1][col]
    return c
