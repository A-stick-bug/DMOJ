# https://dmoj.ca/problem/coci06c5p5
# game theory DP
# you take one, opponent takes one, person with highest score wins

from functools import cache

n = int(input())
arr = list(map(lambda x:int(x)&1, input().split())) * 3

@cache
def solve(l, r):
    if r - l - 1 == n:  # took everything
        return 0
    return max(arr[l] - solve(l - 1, r),  # take left
               arr[r] - solve(l, r + 1))  # take right


total = 0  # get number of possible starts
for i in range(n):
    total += (arr[i] - solve(i + n - 1, i + n + 1)) > 0
print(total)
