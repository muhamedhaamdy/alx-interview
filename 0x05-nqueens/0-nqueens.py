import sys

def print_solution(board):
    '''
    Convert the board configuration to a list of queen positions.

    Args:
    board (list): A 2D list representing the N×N chessboard.

    Returns:
    list: A list of lists where each sublist contains the row and column
          indices of a queen.
    '''
    solution = []
    for row in range(len(board)):
        for col in range(len(board)):
            if board[row][col] == 1:
                solution.append([row, col])
    return solution

def is_safe(board, row, col, N):
    '''
    Check if it's safe to place a queen at board[row][col].

    Args:
    board (list): A 2D list representing the N×N chessboard.
    row (int): The row index to check.
    col (int): The column index to check.
    N (int): The size of the chessboard (N×N).

    Returns:
    bool: True if it's safe to place the queen, False otherwise.
    '''
    # Check this row on the left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on the left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on the left side
    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def solve_nqueens_util(board, col, N, solutions):
    '''
    Use backtracking to find all solutions for the N-Queens problem.

    Args:
    board (list): A 2D list representing the N×N chessboard.
    col (int): The current column index to place a queen.
    N (int): The size of the chessboard (N×N).
    solutions (list): A list to store all the solutions found.

    Returns:
    bool: True if a solution is found, False otherwise.
    '''
    if col >= N:
        solutions.append(print_solution(board))
        return True

    res = False
    for i in range(N):
        if is_safe(board, i, col, N):
            board[i][col] = 1
            res = solve_nqueens_util(board, col + 1, N, solutions) or res
            board[i][col] = 0

    return res

def solve_nqueens(N):
    '''
    Solve the N-Queens problem and print all solutions.

    Args:
    N (int): The size of the chessboard (N×N).

    Returns:
    None
    '''
    board = [[0 for _ in range(N)] for _ in range(N)]
    solutions = []
    solve_nqueens_util(board, 0, N, solutions)
    solutions.sort()
    for solution in solutions:
        print(solution)

if __name__ == "__main__":
    '''
    The main function to handle command-line arguments and initiate the solving process.
    '''
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    solve_nqueens(N)
