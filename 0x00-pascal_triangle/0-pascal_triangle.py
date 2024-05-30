def pascal_triangle(n):
    # Initialize each row with the appropriate number of elements
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
