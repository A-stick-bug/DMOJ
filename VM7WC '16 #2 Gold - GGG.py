# https://dmoj.ca/problem/vmss7wc16c2p3
# longest common subsequence (LCS) DP variation -> longest increasing subsequence DP (LIS)
# note:
# - for both sequences, the elements are unique
# - LCS cannot be solved in faster than O(n^2) so we need to transform the problem

from bisect import bisect_left

n = int(input())
s = list(map(int, input().split()))
m = int(input())
t = list(map(int, input().split()))

loc = {val: i for i, val in enumerate(s)}
index_in_s = []
for i in range(m):
    if t[i] not in loc:  # character is not in s
        continue
    index_in_s.append(loc[t[i]])

# find the LIS of index_in_s
lis = []
for val in index_in_s:
    pos = bisect_left(lis, val)
    if pos == len(lis):
        lis.append(val)
    else:
        lis[pos] = val

print(len(lis))
