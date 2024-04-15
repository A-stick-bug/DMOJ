# https://dmoj.ca/problem/dmopc20c1p3
# note that you can only increase element
# first check the cost of turning the array into decreasing only
# then, we try making it increasing up to i for all indices i (transition in O(1))

n = int(input())
arr = list(map(int, input().split()))

cost = [0] * n  # calculate cost of making everything decreasing
cur_max = arr[-1]
for i in reversed(range(n - 1)):
    cost[i] = max(0, cur_max - arr[i])
    cur_max = max(cur_max, arr[i])

best = sum(cost)
cur_cost = best - cost[0]
best = min(best, cur_cost)

cur_max = arr[0]  # try making it increase up to i
for i in range(1, n):
    cur_cost -= cost[i]
    cur_cost += max(0, cur_max - arr[i])
    cur_max = max(cur_max, arr[i])
    best = min(best, cur_cost)

print(best)
