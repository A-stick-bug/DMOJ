"""
TLE IN PYTHON, NEED TO REMOVE LOG FACTOR, CHECK C++ CODE
https://dmoj.ca/problem/coci21c6p2

Given A, B, find the sub rectangle in a matrix with minimum |sum - A| + |sum - B|

- We can use a 2D PSA to get the sum of a rectangle in O(1)
- We can't brute force all sub-rectangles because it takes O(n^4)
- Instead, we can use binary search since as you do down a row or column, the sum
  will increase, same method used in: https://leetcode.com/problems/search-a-2d-matrix-ii/description/
  - for every point, we consider expanding to every row below, binary search the optimal column

TC: O(n^3*log(n))
"""


class PSA:  # psa is 1 indexed, use 0-indexed queries
    def __init__(self, arr):
        self.psa = [[0] * (len(arr[0]) + 1) for _ in range(len(arr) + 1)]
        for i in range(1, len(arr) + 1):
            for j in range(1, len(arr[0]) + 1):
                self.psa[i][j] = self.psa[i - 1][j] + self.psa[i][j - 1] - self.psa[i - 1][j - 1] + arr[i - 1][j - 1]

    def query(self, r1, c1, r2, c2):
        """query rectangle (r1, c1) to (r2, c2) inclusive"""
        return self.psa[r2 + 1][c2 + 1] - self.psa[r2 + 1][c1] - self.psa[r1][c2 + 1] + self.psa[r1][c1]


N, M, A, B = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
psa = PSA(grid)

best = float('inf')
for i in range(N):
    for j in range(M):  # for every point (i,j) in the grid
        for r in range(i, N):  # try every row below
            low = j
            high = M - 1
            while low <= high:  # binary search the optimal column
                mid = (low + high) // 2
                if psa.query(i, j, r, mid) >= B:
                    high = mid - 1
                else:
                    low = mid + 1

            # also try the columns adjacent to the one we found since they may be more optimal
            for m in range(max(0, low - 1), min(M, low + 2)):
                q = psa.query(i, j, r, m)
                best = min(best, abs(A - q) + abs(B - q))

print(best)
