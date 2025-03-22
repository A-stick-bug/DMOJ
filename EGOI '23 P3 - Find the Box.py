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
"""

import sys

R, C = map(int, input().split())


# attempt 1:
# 2d row sweeps
# 1d column sweep as last step
# if we end at r, the box is in row r+1
# if r = R, the box is in the first row


def ask(arr):
    print("? " + "".join(arr))
    r, c = map(int, input().split())
    return r, c


def check_row(r):
    moves = "v" * r + ">" * C
    return ask(moves)


# construct row sweep
row = "v^>" * C
row = row[:-1]  # remove extra move
row += "<" * (C - 1)
full_sweep = (row + "v") * R

print(len(full_sweep))
row_res, _ = ask(full_sweep)
row_res += 1

if row_res == R:
    # box is in one of the first 2 rows and NOT on the first column
    for r in range(2):
        rr, cc = check_row(r)
        if rr != r:  # didn't get to row
            print("!", rr + 1, 0)
            sys.exit()
        else:
            if cc != C - 1:
                print("!", r, cc + 1)
                sys.exit()

else:
    rr, cc = check_row(row_res)
    if rr != row_res:
        print("!", row_res, 0)
    elif cc != C:
        print("!", row_res, cc + 1)
    else:
        assert 0
