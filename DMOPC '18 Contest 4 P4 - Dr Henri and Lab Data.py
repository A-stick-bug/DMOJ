"""
https://dmoj.ca/problem/dmopc18c4p4
Similar to DMOPC - Selective cutting: https://dmoj.ca/problem/dmopc14c2p6

Fenwick tree + offline processing
Queries are already 1-indexed

First, fill up the < K BIT with all the numbers, the one with >= K numbers is empty
For each query, we first move all numbers >= K from the smaller to the bigger BIT (queries are in descending order)
Now, we can get the query's answer using .query(right) - .query(left - 1)

"""

import sys

input = sys.stdin.readline


class FenwickTree:
    def __init__(self, size):
        if type(size) == int:  # create empty BIT
            self.bit = [0] * (size + 1)
        else:  # create from array
            nums = size
            psa = [0] * (len(nums) + 1)
            for i in range(1, len(nums) + 1):
                psa[i] = psa[i - 1] + nums[i - 1]

            self.bit = [0] * (len(nums) + 1)
            for i in range(1, len(nums) + 1):
                self.bit[i] = psa[i] - psa[i - (i & -i)]

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


N, Q = map(int, input().split())
temp = list(map(int, input().split()))

arr = [(i + 1, int(val)) for i, val in enumerate(temp)]  # (index + 1, value), indexes uses 1-indexing for BIT
arr.sort(reverse=True, key=lambda x: x[1])  # sort by value

queries = [[i] + list(map(int, input().split())) for i in range(Q)]  # (index, left, right, k)
queries.sort(reverse=True, key=lambda x: x[3])  # sort by k
ans = [-1] * Q

greater = FenwickTree(N)
less = FenwickTree(temp)

arr_index = 0
for i, left, right, k in queries:
    while arr_index < N and arr[arr_index][1] >= k:
        index, value = arr[arr_index][0], arr[arr_index][1]
        greater.update(index, value)
        less.update(index, -value)
        arr_index += 1

    greater_k = greater.query(right) - greater.query(left - 1)
    less_k = less.query(right) - less.query(left - 1)
    ans[i] = greater_k - less_k

for a in ans:
    print(a)
