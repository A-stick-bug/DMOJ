# space optimized code that only uses 1 prefix sum matrix

# the parity of (row + col) determines whether it is on a white or black tile
# create 2 prefix sum matrices, one for even and one for odd

import sys

input = sys.stdin.readline

ROWS, COLS = map(int, input().split())
grid = [[0] * (COLS + 1) for _ in range(ROWS + 1)]

while True:
    r, c, val = map(int, input().split())
    if r == 0:  # end of input section
        break

    if (r + c) % 2 == 0:  # set even values positive
        grid[r][c] += val
    else:
        grid[r][c] -= val  # set odd values negative

# thanks to the question's 1-indexing, we don't need to shift the values
# create prefix sum arrays
psa = [[0] * (COLS + 1) for _ in range(ROWS + 1)]
for i in range(1, ROWS + 1):
    for j in range(1, COLS + 1):
        psa[i][j] = psa[i - 1][j] + psa[i][j - 1] + grid[i][j] - psa[i - 1][j - 1]

# handle queries
while True:
    r1, c1, r2, c2 = map(int, input().split())
    if r1 == 0:  # end of queries
        break
    area = psa[r2][c2] - psa[r1 - 1][c2] - psa[r2][c1 - 1] + psa[r1 - 1][c1 - 1]

    if (r1 + c1) % 2 == 0:  # starting cell is even, answer is (white - black)
        print(area)

    # starting cell is odd, answer is (black - white)
    # because our prefix sum counts black as negative, we need to flip the sign
    else:
        print(-area)

# # code doesn't pass in python but writing this exact solution in c++ passes
# # uses too much memory because there are 2 prefix sums
#
# # the parity of (row + col) determines whether it is on a white or black tile
# # create 2 prefix sum matrices, one for even (white) and one for odd (black)
#
# ROWS, COLS = map(int, input().split())
#
# white = [[0] * (COLS + 1) for _ in range(ROWS + 1)]  # even
# black = [[0] * (COLS + 1) for _ in range(ROWS + 1)]  # odd
# while True:
#     r, c, val = map(int, input().split())
#     if r == 0:  # end of input section
#         break
#     if (r + c) % 2 == 0:
#         white[r][c] += val
#     else:
#         black[r][c] += val
#
# # thanks to the question's 1-indexing, we don't need to shift the values
# # create prefix sum arrays
# psa_w = [[0] * (COLS + 1) for _ in range(ROWS + 1)]
# for i in range(1, ROWS + 1):
#     for j in range(1, COLS + 1):
#         psa_w[i][j] = psa_w[i - 1][j] + psa_w[i][j - 1] + white[i][j] - psa_w[i - 1][j - 1]
#
# psa_b = [[0] * (COLS + 1) for _ in range(ROWS + 1)]
# for i in range(1, ROWS + 1):
#     for j in range(1, COLS + 1):
#         psa_b[i][j] = psa_b[i - 1][j] + psa_b[i][j - 1] + black[i][j] - psa_b[i - 1][j - 1]
#
# # handle queries
# while True:
#     r1, c1, r2, c2 = map(int, input().split())
#     if r1 == 0:  # end of queries
#         break
#
#     w_area = psa_w[r2][c2] - psa_w[r1 - 1][c2] - psa_w[r2][c1 - 1] + psa_w[r1 - 1][c1 - 1]
#     b_area = psa_b[r2][c2] - psa_b[r1 - 1][c2] - psa_b[r2][c1 - 1] + psa_b[r1 - 1][c1 - 1]
#
#     if (r1 + c1) % 2 == 0:  # starting cell is even, answer is (white - black)
#         print(w_area - b_area)
#
#     else:  # starting cell is odd, answer is (black - white)
#         print(b_area - w_area)
