# https://dmoj.ca/problem/dmopc16c1p4
# Tree DP
# When joining 2 paths, the expression can be simplified
# TC: O(n^2)

import sys

input = sys.stdin.readline
n = int(input())
val = [-1] + list(map(int, input().split()))
graph = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

total = 0


def solve(cur, prev):
    global total

    def matching(b1):  # O(n)
        t = 0
        for a, b in b1:
            t += (cnt * a * b) + (a * le_sum) + (b * val_sum) + ij_sum
        return t

    paths = [(val[cur], 0)]

    cnt = 1
    val_sum = val[cur]
    le_sum = 0
    ij_sum = 0

    for adj in graph[cur]:
        if adj == prev:
            continue
        c_paths = solve(adj, cur)
        c_paths = [(i, j + 1) for i, j in c_paths]
        total += matching(c_paths)

        cnt += len(c_paths)
        val_sum += sum(i + val[cur] for i, j in c_paths)
        le_sum += sum(j for i, j in c_paths)
        ij_sum += sum((i + val[cur]) * j for i, j in c_paths)
        paths.extend([(i + val[cur], j) for i, j in c_paths])

    return paths


solve(1, -1)
print(total)

"""
5
1 2 3 4 5
1 2
1 3
3 4
3 5

line graph
3
1 2 3
1 2
2 3
"""
