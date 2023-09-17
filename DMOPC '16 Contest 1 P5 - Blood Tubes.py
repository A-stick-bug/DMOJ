"""
https://dmoj.ca/problem/dmopc16c1p5

Inversion counting using Fenwick Tree
Also using a greedy algorithm

For each blood tube, put at the front or at the back, depending on which one creates fewer inversions
Doing this for every blood tube will give the fewest number of inversions at the end
(not sure why greedy works here, but it does, proof by AC 👍)

"""

import sys

input = sys.stdin.readline


class FenwickTree:
    def __init__(self, size):
        self.bit = [0] * size

    def update(self, i: int, diff: int) -> None:
        while i < len(self.bit):
            self.bit[i] += diff
            i += i & (-i)

    def query(self, i: int):
        total = 0
        while i > 0:
            total += self.bit[i]
            i -= i & (-i)
        return total


N = int(input())
arr = list(map(int, input().split()))
bit = FenwickTree(N + 2)

freq = [0] * N  # 0-indexed
for i in arr:
    freq[i - 1] += 1

inversions = 0
for num in arr:
    start = bit.query(num)
    end = bit.query(N+1) - bit.query(num)
    bit.update(num, 1)
    inversions += min(start, end)

print(inversions)
