# https://dmoj.ca/problem/coci06c2p5

# O(MN)
# this is just the largest rectangle in a matrix problem (LC 85) but using perimeter instead of area
# using the 'largest histogram' method (from LC 84)
# print its perimeter MINUS 1 because Mirko himself takes a seat


def largest_histogram(heights):
    heights.append(0)  # this will make sure we check remaining elements in stack after iterating all heights
    stack = []
    res = 0
    for i in range(len(heights)):

        # keep stack in increasing order (strict)
        while stack and heights[stack[-1]] >= heights[i]:
            height = heights[stack.pop()]

            # if the stack is empty, then the current height can extend all the way to the left
            width = i if not stack else i - stack[-1] - 1  # minus one because it is the width between 2 points
            p = perimeter(height, width)
            res = max(res, p)

        stack.append(i)
    return res


def perimeter(x, y):
    if x == 0 or y == 0:
        return 0
    return 2 * (x + y)


ROWS, COLS = map(int, input().split())
matrix = [list(input()) for _ in range(ROWS)]

histogram = [0] * COLS  # build a histogram and update on every row
max_perimeter = 0

for row in matrix:
    for c in range(COLS):  # update histogram
        histogram[c] = (histogram[c] + 1) if row[c] == "." else 0

    # get max area using the current row and every row above it
    max_perimeter = max(max_perimeter, largest_histogram(histogram))

print(max_perimeter - 1)
