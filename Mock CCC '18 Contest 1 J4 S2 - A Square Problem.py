# 1-9, A-Z is in increasing order lexicographically, so we can just compare strings

from collections import Counter

n = int(input())
grid = [list(input()) for _ in range(n)]
flipped = list(zip(*grid))  # swap the rows and columns

# check if rows and cols have unique elements only
if all(len(Counter(row)) == n for row in grid) and all(len(Counter(col)) == n for col in flipped):
    if grid[0] == sorted(grid[0]) and list(flipped[0]) == sorted(flipped[0]):
        print("Reduced")
    else:
        print("Latin")
else:
    print("No")
