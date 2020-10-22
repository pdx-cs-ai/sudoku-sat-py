#!/usr/bin/python3
# Copyright (c) 2016 Bart Massey

# Read DIMACS format SAT solver output
# http://www.satcompetition.org/2009/format-benchmarks2009.html
# to solve a Sudoku instance.

from sys import stdin, stderr

def unlit(b):
    b -= 1
    v = b % 9 + 1
    c = (b // 9) % 9
    r = b // 9 // 9
    return (r, c, v)

board = [[None]*9 for _ in range(9)]

header = next(stdin).strip()
if header == "s SATISFIABLE":
    # picosat
    lines = [l[1:] for l in stdin.readlines() if l and l[0] == 'v']
    solution = [int(b) for l in lines for b in l.split() if int(b) > 0]
elif header == "SAT":
    # minisat
    solution = [int(b) for b in next(stdin).split() if int(b) > 0]
else:
    print("unknown solution format", file=stderr)
    exit(-1)

for n in solution:
    (r, c, v) = unlit(n)
    assert board[r][c] == None
    board[r][c] = v

for r in range(9):
    for c in range(9):
        print(board[r][c], end="")
    print()
