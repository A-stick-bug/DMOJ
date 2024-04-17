# https://dmoj.ca/problem/coci07c4p4
# variation of 0-1 knapsack, lots of painful implementation
# Q: fit people into 2 groups, keep track of who is in what group
# Strategy: fit as many people in group1 using knapsack, put everyone else in group 2
# note that you need to keep track of the state you transitioned from to rebuild the groups

T, N = map(int, input().split())
arr = list(map(int, input().split()))

item = [-1] * (T + 1)
dp = [0] * (T + 1)
dp[0] = 1

for i, time in enumerate(arr):  # 0-1 knapsack
    for t in reversed(range(time, T + 1)):
        if not dp[t] and dp[t - time]:
            item[t] = i
            dp[t] = 1

for i in reversed(range(T + 1)):
    if dp[i]:
        break

res = [-1] * N  # rebuild group 1 using dp stuff
while i > 0:
    res[item[i]] = i - arr[item[i]]
    i -= arr[item[i]]

other_sum = 0  # build group 2 greedily
for i in range(N):
    if res[i] != -1:
        continue
    res[i] = other_sum
    other_sum += arr[i]

print(*res)
