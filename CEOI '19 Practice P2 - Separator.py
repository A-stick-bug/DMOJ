# https://dmoj.ca/problem/ceoi19pp2
# Monotonic stack
# - Each query adds an element to array, count number of elements where
#   everything before is smaller and everything after is bigger
# - Use a monotonic stack to maintain separators in ascending order

import sys

MOD = 10 ** 9
input = sys.stdin.readline
Q = int(input())
separators = []

prev_max = -1  # maximum previous element
for _ in range(Q):
    cur = (int(input()) + len(separators)) % MOD

    # remove all separators with value more than cur since cur is after them and has smaller value
    while separators and separators[-1] > cur:
        separators.pop()

    # cur is a separator if it is greater than anything before
    if prev_max < cur:
        separators.append(cur)

    prev_max = max(prev_max, cur)
    print(len(separators))
