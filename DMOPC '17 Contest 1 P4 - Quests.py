# TLE, CHECK C++ CODE
# https://dmoj.ca/problem/dmopc17c1p4
# Mixed knapsack
# Part 1: 0/1 knapsack
# Part 2: unbounded knapsack
#
# TC: O(N * H)

def solve():
    inf = 1 << 60
    N, H = map(int, input().split())
    prev1 = [-inf] * (H + 1)  # did not take previous set
    prev2 = [-inf] * (H + 1)

    prev1[0] = prev2[0] = 0

    # (val, cost), (val, cost)
    for _ in range(N):
        v1, c1, v2, c2 = map(int, input().split())

        # 0/1 first for going to the NPCs
        dp2 = [-inf] * (H + 1)
        dp1 = [max(i, j) for i, j in zip(prev1, prev2)]  # not taking from this set

        for v in reversed(range(c1, H + 1)):
            dp2[v] = dp1[v - c1] + v1

        # unbounded for doing amounts of quests
        for v in range(c2, H + 1):
            dp2[v] = max(dp2[v], dp2[v - c2] + v2)

        prev1 = dp1
        prev2 = dp2

    print(max(max(prev1), max(prev2)))


solve()

"""
2 7
9 1 7 1
5 3 2 1
7 1 4 3
1 2 8 1
"""
