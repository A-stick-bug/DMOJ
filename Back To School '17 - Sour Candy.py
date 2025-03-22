# https://dmoj.ca/problem/bts17p6
# Multi-step problem, use Fenwick Tree for answer extraction
# - First simplify the problem by combining the 2 arrays into 1 by mapping indices
# - Our goal is now to sort the new array
# - Optimal strategy: keep the longest consecutive subsequence (eg. x, x+1, x+2, ... x+k)
#
# To print the sequence of moves:
# - Maintain an array that allows for shifting ranges of indices with the help of a Fenwick Tree
# - Note that not all indices are correct, since we don't care about the stuff we already moved


class FenwickTree:  # range update, point query, 1-indexed
    def __init__(self, n):
        self.bit = [0] * (n + 1)

    def add(self, i, val):
        while i < len(self.bit):
            self.bit[i] += val
            i += i & -i

    def range_add(self, l, r, val):
        self.add(l, val)
        self.add(r + 1, -val)

    def query(self, i):
        ret = 0
        while i > 0:
            ret += self.bit[i]
            i -= i & -i
        return ret


n = int(input())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

loc = {}
for i, v in enumerate(arr2):
    loc[v] = i

# simplify problem -> goal is to sort arr
arr = [0] * n
for i in range(n):
    arr[i] = loc[arr1[i]]

# compute longest consecutive subsequence, use uniqueness constraint
loc_arr = [-1] * n
for i, v in enumerate(arr):
    loc[v] = i

dp = [1] * n
for i in range(1, n):
    if loc[i - 1] < loc[i]:
        dp[i] = dp[i - 1] + 1

# [low,high] represents longest consecutive
high = dp.index(max(dp))
low = high - dp[high] + 1

# print("arr", arr)
# print(low, high)
# print("dp", dp)

# correctly move everything that is not part of the consecutive numbers
shift = FenwickTree(n)
moves = []
for i in reversed(range(low)):
    idx = loc[i] + shift.query(loc[i] + 1)  # 1-indexed
    moves.append("F " + str(idx + 1))
    shift.range_add(1, loc[i] + 1, 1)  # insert to front, shift right

for i in range(high + 1, n):
    idx = loc[i] + shift.query(loc[i] + 1)
    moves.append("B " + str(idx + 1))
    shift.range_add(loc[i] + 1, n, -1)  # insert to back, shift left

print(len(moves))
print("\n".join(map(str, moves)))

"""
Example case:
5
5 1 2 3 4
1 3 2 5 4

3
B 3
B 1
B 3
"""
