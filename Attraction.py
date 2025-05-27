"""
https://dmoj.ca/problem/attraction
Why is everyone using heap/priority queues???

Greedy, observation heavy, a lot of casework
Note: all observations can be proved fairly easily by induction

Even gaps:
- First, put a B right next to the A on the left, this gets half (AB_____A)
- Second, put a B on the other end, this gets the other half (AB____BA)

Odd gaps:
- n = 1: put B right on it  (ABA)
- n = 3
  - first move, put a B on the left, this gets 2 cells (AB__A)
  - can't get anything on second move, get last cell on third move (ABBBA)
  - since the sequence is [2,0,1], consider it as using 2 moves to get 1 cell
- n > 3:
  - First, put a B right next to the A on the left, this gets ceil(N/2) cells (AB______A)
  - Second, put a B on the other end, this takes all but 1 cell in the center (AB_____BA)
  - Third, take all in the gap by turning it into even (ABB____BA)
"""

import sys

input = sys.stdin.readline


def solve():
    N, A, B = map(int, input().split())
    arr = list(map(int, input().split()))

    # get 'gaps'
    arr.sort()
    gaps = [arr[i] - arr[i - 1] - 1 for i in range(1, A)]

    # Knapsack-like
    # We can sort since the gains from an individual gap are always in decreasing order
    # (Except n=3 which is handled independently)
    options = []
    options.append(arr[0] - 1)  # start
    options.append(N - arr[-1])  # end

    two_moves = 0  # for n=3 case
    for val in gaps:
        if val == 0:  # useless
            continue
        elif val == 1:  # place 1 'B' to cover it
            options.append(1)
        elif val == 3:  # SPECIAL CASE
            options.append(2)
            two_moves += 1
        else:  # normal cases
            if val % 2 == 0:
                options.append(val // 2)
                options.append(val // 2)
            else:
                v1 = (val + 1) // 2
                v2 = val - v1 - 1
                v3 = 1
                options.extend([v1, v2, v3])

    options.sort(reverse=True)
    while options and options[-1] == 0:  # remove useless zeros
        options.pop()

    if B <= len(options):  # take highest
        print(sum(options[:B]))
    else:
        extra = B - len(options)  # take all + the ones that use 2 moves
        print(sum(options) + min(extra // 2, two_moves))


t = int(input())
for _ in range(t):
    solve()
