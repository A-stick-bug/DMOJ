from sys import stdin

input = stdin.readline

N_ROWS, N_COLS = map(int, input().split())
rows = [False for _ in range(N_ROWS)]
cols = [False for _ in range(N_COLS)]

for r in range(N_ROWS):
    line = input()
    for c, cell in enumerate(line):
        if cell == "X":
            rows[r] = True 
            cols[c] = True

for _ in range(int(input())):
    col, row = map(int, input().split())
    if rows[row - 1] or cols[col - 1]:
        print("Y")
    else:
        print("N")
