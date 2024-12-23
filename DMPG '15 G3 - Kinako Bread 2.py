# https://dmoj.ca/problem/dmpg15g3
# Find # of paths satisfying condition in tree -> centroid decomposition
#
# Matching subtree paths: treat as a 2D grid and use 2D fenwick tree (MLE)
# Optimization: Compress to 1D with line sweep
# - x-dimension: sort by x and use 2 pointers to form a valid 'range'
# - y-dimension: fenwick tree to query number of paths satisfying condition
#
# TC: O(n*log^2(n))

import sys


class FenwickTree:  # point update, range query, 1-indexed
    def __init__(self, size):
        """Create empty Fenwick Tree"""
        self.bit = [0] * (size + 1)

    def update(self, i: int, diff) -> None:
        """Add diff to self.bit[i]"""
        while i < len(self.bit):
            self.bit[i] += diff
            i += i & (-i)

    def query(self, i: int):
        """Get the sum up to the i-th element (inclusive)"""
        total = 0
        while i > 0:
            total += self.bit[i]
            i -= i & (-i)
        return total

    def query_range(self, left: int, right: int):
        """Query the sum of elements from left to right, inclusive"""
        return self.query(right) - self.query(left - 1)


input = sys.stdin.readline
sys.setrecursionlimit(200000)

N, LX, RX, LY, RY = map(int, input().split())
arr = [(-1, -1)] + [(1, 0) if i == "K" else (0, 1) for i in input().strip()]
graph = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

sz = [0] * (N + 1)
cut = [False] * (N + 1)  # determine is node i is removed
total = 0
bit = FenwickTree(N + 1)


def get_sizes(cur, prev):
    """get subtree sizes of a subtree/component"""
    sz[cur] = 1
    for adj in graph[cur]:
        if adj == prev or cut[adj]:
            continue
        get_sizes(adj, cur)
        sz[cur] += sz[adj]


def get_centroid(cur, prev, comp_size):
    """find the centroid of a subtree/component"""
    for adj in graph[cur]:
        if not cut[adj] and adj != prev and sz[adj] > comp_size // 2:
            return get_centroid(adj, cur, comp_size)
    return cur


def get_paths(cur, prev):
    """get all path values ending in cur's subtree"""
    stack = [(arr[cur][0], arr[cur][1], cur, prev)]
    paths = []
    while stack:
        x, y, cur, prev = stack.pop()
        paths.append((x, y))
        for adj in graph[cur]:
            if not cut[adj] and adj != prev:
                stack.append((x + arr[adj][0], y + arr[adj][1], adj, cur))
    return paths


def match_pairs(paths, lx, rx, ly, ry):
    """match paths satisfying lx <= sum(x) <= rx and ly <= sum(y) <= ry
    Use 2-pointers (similar to line sweep) and Fenwick tree"""
    paths.sort(key=lambda x: x[0])

    def helper(rx):
        if rx < 0:
            return 0
        l = -1
        t = 0
        for r in reversed(range(len(paths))):
            while l + 1 < r and paths[r][0] + paths[l + 1][0] <= rx:
                l += 1
                bit.update(paths[l][1] + 1, 1)
            if l >= r:
                bit.update(paths[l][1] + 1, -1)
                l -= 1
            t += bit.query_range(ly - paths[r][1] + 1, ry - paths[r][1] + 1)

        # assert all(i == 0 for i in bit.bit)  # tree should be empty when we're done
        return t

    return helper(rx) - helper(lx - 1)


def solve(root):
    global total
    get_sizes(root, -1)
    centroid = get_centroid(root, -1, sz[root])  # centroid of this component
    cx, cy = arr[centroid]

    # collect subtree paths
    # note: they do NOT include the value of the current node so we minus that when matching pairs
    all_paths = [(0, 0)]
    for adj in graph[centroid]:
        if cut[adj]:
            continue
        paths = get_paths(adj, centroid)
        # remove matches from the same subtree
        total -= match_pairs(paths, LX - cx, RX - cx, LY - cy, RY - cy)
        all_paths.extend(paths)

    total += match_pairs(all_paths, LX - cx, RX - cx, LY - cy, RY - cy)

    # recurse to children
    cut[centroid] = True  # cut off node
    for adj in graph[centroid]:  # solve for all subtrees
        if not cut[adj]:
            solve(adj)


solve(1)

# check if individual nodes satisfies condition
for x, y in arr:
    if LX <= x <= RX and LY <= y <= RY:
        total += 1

print(total)

"""
For visualizing the graph here: https://csacademy.com/app/graph_editor/
1X 2Y
1X 3Y
2Y 4X
1X 5Y
3Y 6X
3Y 7X
6X 8Y
5Y 9X
5Y 10X

Custom test case (answer: 19)
10 0 1 0 1
KCCKCKKCKK
1 2
1 3
2 4
1 5
3 6
3 7
6 8
5 9
5 10

def match_pairs_slow(paths, lx, rx, ly, ry):
    # brute force pair matching (this is just here for reference)
    # match paths satisfying lx <= sum(x) <= rx and ly <= sum(y) <= ry
    t = 0
    for i in range(len(paths)):
        for j in range(i + 1, len(paths)):
            if lx <= paths[i][0] + paths[j][0] <= rx and ly <= paths[i][1] + paths[j][1] <= ry:
                t += 1
    return t
"""
