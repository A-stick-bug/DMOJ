"""
TLE, PYTHON IS TOO SLOW, CHECK C++ CODE

https://dmoj.ca/problem/ioi11p2io
Tree all-paths questions
At each node, we store the paths in {sum: min length to achieve sum} for efficient joining
As usual we use 2-sum method to join paths (also consider only using 1 path)

Now we have 2 approaches:
1. Standard tree DP with small to large merging of children and offsetting
   for fast children-to-parent transitions
2. Template centroid decomposition

I'll be using the second method because offsetting to do the transitions is very annoying
TC: O(nlogn)
"""
import sys

inf = 1 << 30
input = sys.stdin.readline
sys.setrecursionlimit(100000)

N, K = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

best = inf
size = [0] * (N + 1)
cut = [False] * (N + 1)  # determine is node i is removed


def get_sizes(cur, prev):
    size[cur] = 1
    for adj, _ in graph[cur]:
        if adj == prev or cut[adj]:
            continue
        get_sizes(adj, cur)
        size[cur] += size[adj]


def get_centroid(cur, prev, comp_size):
    for adj, _ in graph[cur]:
        if not cut[adj] and adj != prev and size[adj] > comp_size // 2:
            return get_centroid(adj, cur, comp_size)
    return cur


def get_paths(start, prev):
    stack = [(start, prev, 0, 0)]  # cur, prev, sum, length
    paths = []
    while stack:
        cur, prev, tot, le = stack.pop()
        paths.append((tot, le))
        for adj, val in graph[cur]:
            if adj == prev or cut[adj]:
                continue
            stack.append((adj, cur, tot + val, le + 1))
    return paths


def solve(node):
    global best
    get_sizes(node, -1)
    centroid = get_centroid(node, -1, size[node])
    match = {0: 0}  # include option of only using 1 path

    for adj, val in graph[centroid]:
        if cut[adj]:
            continue
        # include the edge from centroid to adj
        adj_paths = list(map(lambda x: (x[0] + val, x[1] + 1), get_paths(adj, centroid)))
        for tot, le in adj_paths:  # match current subtree's paths with others
            if K - tot in match:
                best = min(best, match[K - tot] + le)  # joined 2 path to sum to K
        for tot, le in adj_paths:  # add current subtree's paths as a matching option
            if tot in match:
                match[tot] = min(match[tot], le)
            else:
                match[tot] = le

    cut[centroid] = True  # remove centroid and recurse to subtrees
    for adj, _ in graph[centroid]:
        if not cut[adj]:
            solve(adj)


solve(0)
print(best if best != inf else -1)
