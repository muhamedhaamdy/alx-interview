# N Queens

## Overview

The N Queens problem is a classic computer science problem involving the placement of N chess queens on an N×N chessboard such that no two queens threaten each other. This means that no two queens can share the same row, column, or diagonal.

## Problem Statement

Given an integer N, determine all possible ways to place N queens on an N×N chessboard such that no two queens attack each other. Each solution should be represented as a list of strings, where each string represents a row of the chessboard and contains a '.' for an empty square and a 'Q' for a queen.

## Requirements

- Implement a function `solveNQueens(N)` that returns a list of all distinct solutions to the N Queens problem.
- Each solution should be a list of strings where 'Q' and '.' indicate a queen and an empty space, respectively.

## Example

### Example

```bash
julien@ubuntu:~/0x08. N Queens$ ./0-nqueens.py 4
[[0, 1], [1, 3], [2, 0], [3, 2]]
[[0, 2], [1, 0], [2, 3], [3, 1]]
julien@ubuntu:~/0x08. N Queens$ ./0-nqueens.py 6
[[0, 1], [1, 3], [2, 5], [3, 0], [4, 2], [5, 4]]
[[0, 2], [1, 5], [2, 1], [3, 4], [4, 0], [5, 3]]
[[0, 3], [1, 0], [2, 4], [3, 1], [4, 5], [5, 2]]
[[0, 4], [1, 2], [2, 0], [3, 5], [4, 3], [5, 1]]
julien@ubuntu:~/0x08. N Queens$ 