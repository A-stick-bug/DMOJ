# PYTHON IS TOO SLOW, CHECK C++ CODE
#
# https://dmoj.ca/problem/oly21practice9
# Binary search with greedy idea:
# - put everything with different >threshold in the other region
# - fill the bottom-right sub rectangles of every cell in the other region
#   - we can use a 2D PSA method
# - if the other region has (max-min) < threshold, it works
#
# Note: since there are 4 possible diagonal shapes (including symmetric ones)
#       we must try all of them

def works(grid, diff) -> bool:
    """Check if we can achieve a (max-min) of diff in both regions"""
    marked = [[False] * (C + 1) for _ in range(R + 1)]  # 1-indexed difference array
    for i in range(R):
        for j in range(C):
            # every cell with larger than diff difference must be in the other region
            if largest - grid[i][j] > diff:
                marked[i + 1][j + 1] = True

    # fill in the bottom-right sub-rectangles of marked cells to make diagonal
    for i in range(1, R + 1):
        for j in range(1, C + 1):
            marked[i][j] += marked[i - 1][j] + marked[i][j - 1] - marked[i - 1][j - 1]

    # special case: no cells marked means (max-min) threshold is already satisfied
    # and we can put any cell in the other region
    marked_cnt = sum(marked[i][j] != 0 for i in range(1, R + 1) for j in range(1, C + 1))
    if marked_cnt == 0:
        return True

    # check if the other region's difference is also <=diff
    small = min(grid[i][j] for i in range(R) for j in range(C) if marked[i + 1][j + 1])
    big = max(grid[i][j] for i in range(R) for j in range(C) if marked[i + 1][j + 1])
    return big - small <= diff


def check(diff) -> bool:
    """Check if any of the 4 orientations work"""
    return (works(grid, diff) or
            works(grid[::-1], diff) or
            works([r[::-1] for r in grid], diff) or
            works([r[::-1] for r in grid][::-1], diff))


R, C = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(R)]
largest = max(max(row) for row in grid)

low = 0
high = 10 ** 9
while low <= high:
    mid = (low + high) // 2
    if check(mid):
        high = mid - 1
    else:
        low = mid + 1

print(low)
