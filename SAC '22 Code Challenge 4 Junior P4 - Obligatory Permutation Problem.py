# https://dmoj.ca/problem/sac22cc4jp4
# classic cycle detection problem
# note that each element will be in exactly 1 cycle

def get_cycle(start):
    cycle = [start]
    cur = arr[start]
    while cur != start:
        cycle.append(cur)
        cur = arr[cur]
    return cycle


N, K = map(int, input().split())
arr = [-1] + list(map(int, input().split()))  # 1-indexing
vis = [False] * (N + 1)
res = [-1] * (N + 1)

for i in range(1, N + 1):
    if vis[i]:  # prevent processing the same index twice since we are processing entire cycles together
        continue
    cycle = get_cycle(i)
    for idx, j in enumerate(cycle):  # process every index in this cycle
        vis[j] = True
        res[cycle[(idx + K) % len(cycle)]] = arr[j]  # where the current number will end up after K moves

print(*res[1:])

"""
Observations
5 10
2 3 1 5 4

[-1, 1, 2, 3, 4, 5]
[-1, 3, 1, 2, 5, 4]
[-1, 2, 3, 1, 4, 5]
[-1, 1, 2, 3, 5, 4]
[-1, 3, 1, 2, 4, 5]
[-1, 2, 3, 1, 5, 4]
[-1, 1, 2, 3, 4, 5]
[-1, 3, 1, 2, 5, 4]
[-1, 2, 3, 1, 4, 5]
[-1, 1, 2, 3, 5, 4]
"""
