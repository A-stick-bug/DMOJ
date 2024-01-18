"""
https://dmoj.ca/problem/sac22cc4p4
similar to https://leetcode.com/problems/count-of-range-sum/ which uses sum instead of min/max

Sliding window with monotonic queues
Right pointer increases by 1 every time
Move left pointer until we are below threshold (queues are used to check this)

"""
from collections import deque


def solve(threshold):
    """get the number of subarrays with max() - min() <= threshold"""
    maxq = deque()
    minq = deque()
    res = 0
    left = 0
    for right in range(N):
        while minq and arr[right] < arr[minq[-1]]:  # keep queues monotonic
            minq.pop()
        minq.append(right)
        while maxq and arr[right] > arr[maxq[-1]]:
            maxq.pop()
        maxq.append(right)

        # move left pointer until we are below the threshold
        while minq and maxq and arr[maxq[0]] - arr[minq[0]] > threshold:
            if minq[0] == left:
                minq.popleft()
            if maxq[0] == left:
                maxq.popleft()
            left += 1
        res += right - left + 1  # all subarrays starting from [l,r] and ending at r are valid

    return res


N, L, H = map(int, input().split())
arr = list(map(int, input().split()))
print(solve(H) - solve(L - 1))

# 8 -999 89
# 1 4 5 2 2 -3 -5 -6

# """
# TLE, NEED O(N) SOLUTION
#
# (max - min) of a subarray as you add more elements to it is a monotonically increasing function (as both are idempotent)
# so we can use binary search + sparse table to get the largest subarray ending at every right (binary search for left)
# now we know every subarray in between also satisfies the condition so add (right - left + 1)
# TC: O(nlogn)
# """
#
# log2 = lambda x: x.bit_length() - 1
#
#
# class SparseTable:  # 0-indexed
#     def __init__(self, arr, f=max, default=0):
#         N = len(arr)
#         self.layers = log2(len(arr)) + 1
#         self.table = [[default] * self.layers for _ in range(len(arr))]
#         self.f = f
#         for i in range(len(arr)):  # base layer
#             self.table[i][0] = arr[i]  # column 1: base cases
#
#         for k in range(1, self.layers):  # build the rest of the table
#             for i in range(N - (1 << k) + 1):
#                 self.table[i][k] = f(self.table[i][k - 1], self.table[i + (1 << (k - 1))][k - 1])
#
#     def query(self, l, r):
#         k = log2(r - l + 1)
#         return self.f(self.table[l][k], self.table[r - (1 << k) + 1][k])
#
#
# def find_left(high, threshold):
#     upper = high  # upper bound
#     low = 0
#     while low <= high:
#         mid = (low + high) // 2
#         if maxs.query(mid, upper) - mins.query(mid, upper) > threshold:
#             low = mid + 1
#         else:
#             high = mid - 1
#     return low
#
#
# N, L, H = map(int, input().split())
# arr = list(map(int, input().split()))
# mins = SparseTable(arr, min, 1 << 30)
# maxs = SparseTable(arr, max, -(1 << 30))
#
# total = 0
# for right in range(N):
#     top = right - find_left(right, H) + 1
#     bot = right - find_left(right, L - 1) + 1
#     total += top - bot
#
# print(total)
