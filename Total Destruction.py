# https://dmoj.ca/problem/totaldestruction
# Simple greedy
# We want to take as little numbers that are not in `arr` as possible
# Since we have M moves we can use them to avoid taking the largest gaps

import sys

input = sys.stdin.readline
MN, M, N = map(int, input().split())
arr = [int(input()) for _ in range(N)]
arr.sort()

if M >= N:  # corner case, make all ranges 1
    print(N)
    sys.exit()

diff = [arr[i + 1] - arr[i] for i in range(N - 1)]
diff.sort(reverse=True)  # avoid largest gaps
print(sum(diff[M - 1:]) + M)
