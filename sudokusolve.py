#!/usr/bin/python3
# Copyright (c) 2016 Bart Massey

# Read DIMACS format SAT solver output
# http://www.satcompetition.org/2009/format-benchmarks2009.html
# to solve a Sudoku instance.

from sys import stdin

def unlit(b):
    b -= 1
    v = b % 9 + 1
    c = (b // 9) % 9
    r = b // 9 // 9
    return (r, c, v)

board = [[None]*9 for _ in range(9)]

solution = stdin.readlines()
for b in solution:
    n = int(b)
    if n <= 0:
        continue
    (r, c, v) = unlit(n)
    assert board[r][c] == None
    board[r][c] = v

for r in range(9):
    for c in range(9):
        print(board[r][c], end="")
    print()
