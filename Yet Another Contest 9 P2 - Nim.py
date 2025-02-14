# https://dmoj.ca/problem/yac9p2
# note: doing one subtask at a time really helps
#
# Nim, but you choose the next pile that your opponent picks from
# Person who removes last stone wins
#
# With non 1s you can turn it into `1` and force your opponent to take it on the next move
# Now, it's your turn again, so you can basically remove non 1s for free
#
# With only `1`s remaining, you just alternate turns taking them so parity decides the winner
#
# Note: this is proof by AC, I cannot prove why this is optimal

import sys

input = sys.stdin.readline


def solve():
    n = int(input())
    arr = list(map(int, input().split()))

    ones = arr.count(1)

    if ones % 2 == 0:
        print("Mike")
    else:
        print("Josh")


for _ in range(int(input())):
    solve()
