"""
https://dmoj.ca/problem/dpk
1D Game theory DP
Basically just flip between winning and losing states because they alternate turns
"""

# Method 2 (faster): If the current state is a losing state, mark future states reachable from the current as winning
N, K = map(int, input().split())  # N possible moves, K stones in total
stones = list(map(int, input().split()))
stones.sort()

dp = [False] * (K + 1)

for i in range(K + 1):
    if not dp[i]:  # current state is losing so any state that can force this state wins
        for stone in stones:
            if i + stone > K:  # optimization: since stones are sorted, we can break early
                break
            dp[i + stone] = True

if dp[-1]:
    print("First")
else:
    print("Second")

# Method 1, check if the current state is a winning state based on previous states
# N, K = map(int, input().split())  # N possible moves, K stones in total
# stones = list(map(int, input().split()))
# stones.sort()
#
# dp = [0] * (K + 1)
#
# for i in range(1, K + 1):
#     for stone in stones:
#         if i - stone < 0:
#             break
#         if not dp[i - stone]:
#             dp[i] = True
#
# if dp[-1]:
#     print("First")
# else:
#     print("Second")
