# https://dmoj.ca/problem/aac2p2
# if arithmetic sequence exists, we can get 3
# of 2 of same parity exists, we can get 2
# otherwise, we can get 1
#
# To find arithmetic sequence, dp works but since its only length 3, we can brute force
# all first 2 numbers and check if third one exists

from bisect import bisect_left
import sys

n = int(input())
arr = list(map(int, input().split()))
arr.sort()

total = 0
for i in range(n):
    for j in range(i + 1, n):
        target = arr[j] + (arr[j] - arr[i])
        if target <= arr[-1] and arr[bisect_left(arr, target)] == target:
            print(3)
            sys.exit()

even = [i for i in arr if i % 2 == 0]
odd = [i for i in arr if i % 2 == 1]
if len(even) > 1 or len(odd) > 1:
    print(2)
else:
    print(1)
