#!/usr/bin/python3
'''nqueens problem'''
import sys
# if len(sys.argv) != 2:
#     print('Usage: nqueens N')
#     sys.exit(1)

# n = sys.argv[1]
# if not n.isdigit():
#     print('N must be a number')
#     sys.exit(1)

# n = int(n)
# if n < 4:
#     print('N must be at least 4')
#     sys.exit(1)

# n = 6

# sol = []
# stack = []
# board = [[0 for _ in range(n)] for _ in range(n)]
# visited = []

# def copy_arr(array):
#     return [row[:] for row in array]

# def remove_duplicates(board_list):
#     seen = set()
#     unique_boards = []
#     for board in board_list:
#         # Convert board to tuple to make it hashable
#         board_tuple = tuple(tuple(row) for row in board)
#         if board_tuple not in seen:
#             unique_boards.append(board)
#             seen.add(board_tuple)
#     return unique_boards

# def is_save(row, col, board):
#     if board[row][col]:
#         return False
#     for i in range(0, n):
#         if board[i][col]:
#             return False
#     for i in range(0, n):
#         if board[row][i]:
#             return False
#     r, c = (row, col)
#     while r < n and c < n:
#         if board[r][c]:
#             return False
#         r += 1
#         c += 1
#     r, c = (row, col)
#     while r >= 0 and c >= 0:
#         if board[r][c]:
#             return False
#         r -= 1
#         c -= 1
#     r, c = (row, col)
#     while r < n and c >= 0:
#         if board[r][c]:
#             return False
#         r += 1
#         c -= 1
#     r, c = (row, col)
#     while r >= 0 and c < n:
#         if board[r][c]:
#             return False
#         r -= 1
#         c += 1

#     return True

# def knigh_move(row, col, board):
#     knigh = [(2,1), (2,-1), (-2,1), (-2,-1), (1,2), (1,-2), (-1,2), (-1,-2)]
#     for (r, c) in knigh:
#         board_copy = copy_arr(board)
#         if row + r < n and row + r >= 0 and col + c < n and col + c >= 0 and is_save(row + r, col + c, board):
#             board_copy[row + r][col + c] = 1
#             stack.append(board_copy)

# def solved_board(board):
#     for i in range(n):
#         for j in range(n):
#             if board[i][j] == 1:
#                 if not is_save(i, j, board):
#                     return False
#     return True

# def queen_position(board):
#     queen_pos = []
#     for i in range(n):
#         for j in range(n):
#             if board[i][j] == 1:
#                 queen_pos.append([i, j])
#     return queen_pos

# def print_board(board):
#     for row in board:
#         print(row)
#     print()

# if __name__ == '__main__':
#     for i in range(n):
#         board[0][i] = 1
#         stack.append(copy_arr(board))
#         board[0][i] = 0    
#     while stack:
#         board = stack.pop(0)
#         for i in range(n):
#             for j in range(n):
#                 if board[i][j] == 1 and (i, j) not in visited:
#                     visited.append((i, j))
#                     knigh_move(i, j, board)
#                     print_board(board)
#         if solved_board(board):
#             sol.append(board)
#         if sum([sum(row) for row in board]) == n:
#             sol.append(board)
#     sol = remove_duplicates(sol)
#     for board in sol:
#         print(queen_position(board))

def print_solution(board):
    solution = []
    for row in range(len(board)):
        for col in range(len(board)):
            if board[row][col] == 1:
                solution.append([row, col])
    print(solution)

def is_safe(board, row, col, N):
    # Check this row on left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on left side
    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def solve_nqueens_util(board, col, N):
    if col >= N:
        print_solution(board)
        return True

    res = False
    for i in range(N):
        if is_safe(board, i, col, N):
            board[i][col] = 1
            res = solve_nqueens_util(board, col + 1, N) or res
            board[i][col] = 0

    return res

def solve_nqueens(N):
    board = [[0 for _ in range(N)] for _ in range(N)]
    if not solve_nqueens_util(board, 0, N):
        print("Solution does not exist")
        return

if __name__ == "__main__":
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
