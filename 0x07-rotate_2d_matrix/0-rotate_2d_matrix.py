#!/usr/bin/python3
''' rotate 2d matrix '''


def rotate_2d_matrix(matrix):
    ''' rotate 2d matrix '''
    transpose_square_matrix(matrix)
    reverse_rows(matrix)


def transpose_square_matrix(matrix):
    ''' transpose a square matrix in place '''
    n = len(matrix)
    for i in range(n):
        for j in range(i+1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]


def reverse_rows(matrix):
    ''' reverse each row in place '''
    for row in matrix:
        row.reverse()
