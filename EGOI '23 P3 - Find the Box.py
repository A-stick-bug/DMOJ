"""
https://dmoj.ca/problem/egoi23p3

Observations:
2 moves -> maybe 1 move to find x coordinate, 1 move to find y

Trivial 50 moves solution:
- Clear first column, then, for each row, go down to it and go right
- Basically clear out L shapes

Weird 9 moves solution:
- Clear out a square with 2 `L`s and binary search rows, find within column in 1 move

3 move solution:
- Do a sweep on every row to find what row the box is in
- Then find what column on the row it is in
- Note: this can't distinguish row 1 and 2, so it takes 3 moves in that case

2 move solution:
- Improve the 3 move solution by sweeping in a specific way
- Now it only has to distinguish an L shape which is trivial
"""
import sys

R, C = map(int, input().split())


def ask(arr):
    print("? " + "".join(arr))
    r, c = map(int, input().split())
    return r, c


def check_row(r):
    moves = "v" * r + ">" * C
    return ask(moves)


# construct main sweep
row = "v^>" * C
row += "v"
row += "<" * C
row += "^<v"

full_sweep = row * R

row_res, _ = ask(full_sweep)
row_res += 1

if row_res == R:  # didn't get blocked, answer is either in (first row) or (second row + last column)
    rr, cc = check_row(0)
    if cc != C - 1:  # in first row
        print("!", 0, cc + 1)
        sys.exit()
    else:  # in second row + last column
        print("!", 1, C - 1)
        sys.exit()

else:  # got blocked, located the exact row, check column with L shape
    rr, cc = check_row(row_res)
    if rr != row_res:
        print("!", row_res, 0)
    elif cc != C:
        print("!", row_res, cc + 1)
    else:
        assert 0
