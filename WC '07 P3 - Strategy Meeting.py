# MLE, PYTHON USES TOO MUCH MEMORY
#
# https://dmoj.ca/problem/wc07p3
# Q: given a graph, find the number of distinct paths from 0 to N-1
# A: brute force DFS, keep track of all nodes visited so far on this path (use bitmask for this) and current node

# ---------------- BITWISE TEMPLATE START -------------

# note: index of bits are 0-indexed
def set_bit(n, i, val):
    """set the i-th bit of n"""
    if val == 1:
        return n | (1 << i)
    else:
        return ~(1 << i) & n


def get_bit(n, i):
    """returns whether the i-th bit of n is on"""
    return n & (1 << i)


# ---------------- BITWISE TEMPLATE END --------------

def solve():
    n = int(input())
    graph = [list(map(int, input().split())) for _ in range(n)]
    cache = [[-1] * (1 << n) for _ in range(n)]

    def dfs(cur, mask):
        if cur == n - 1:
            return 1
        if cache[cur][mask] != -1:
            return cache[cur][mask]
        total = 0
        for adj, val in enumerate(graph[cur]):
            if not val:  # no edge here
                continue
            if mask & (1 << adj):  # already visited on this path
                continue
            total += dfs(adj, mask | (1 << adj))
        cache[cur][mask] = total
        return total

    print(dfs(0, 1))


for _ in range(int(input())):
    solve()
