# https://dmoj.ca/problem/noip99p3
# Note: the current code can be optimized to O(nlogn) using data structures
# Greedy, at each index consider 3 cases
# 1. no gas station in range: impossible
# 2. cheaper gas station in range: go to first cheaper one
# 3. more expensive ones in range: fully fill at the current station, go to cheapest one available
#
# TC: O(n^2)

total_d, capacity, eff, price1, n = map(float, input().split())
arr = [list(map(float, input().split())) for _ in range(int(n))]  # location, fuel cost
arr.append([0, price1])  # initial
arr.append([total_d, -1])  # final
n = len(arr)

arr.sort()
inf = 1 << 60


def solve(cur, fuel):
    if cur == n - 1:
        return 0

    cur_loc, cur_cost = arr[cur]

    possible = []  # possible next stations
    for nxt in range(cur + 1, n):
        loc, cost = arr[nxt]
        if loc - cur_loc <= eff * capacity:
            possible.append(nxt)

    # case 1: can't reach anything
    if not possible:
        return inf

    # case 2: can reach a smaller cost, go to first one
    for nxt in possible:
        loc, cost = arr[nxt]
        if cost <= cur_cost:
            fuel_req = (loc - cur_loc) / eff
            used = min(fuel_req, fuel)
            bought = fuel_req - used
            return solve(nxt, fuel - used) + cur_cost * bought

    # case 3: can't reach a smaller cost, find cheapest
    best_nxt = cur + 1
    for nxt in possible:
        loc, cost = arr[nxt]
        if arr[best_nxt][1] > cost:
            best_nxt = nxt

    loc, cost = arr[best_nxt]
    fuel_req = (loc - cur_loc) / eff
    bought = capacity
    return solve(best_nxt, bought - fuel_req) + cur_cost * bought


ans = solve(0, 0)
if ans < inf:
    print(f"{ans:.2f}")
else:
    print("No Solution")
