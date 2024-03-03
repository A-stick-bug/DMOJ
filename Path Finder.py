"""
https://dmoj.ca/problem/pathfind
Graph theory, with slightly different logic

Note that there are 500000 rows and columns, so we can't do O(RC) DFS.
Instead, we just check if there is a 'path on walls' that connect the (left/bottom) to (right/top) part of the grid

TC: O(K)
"""

import sys

input = sys.stdin.readline
R, C, K = map(int, input().split())
blocked = {tuple(map(int, input().split())) for _ in range(K)}

dir = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]


def dfs(start):
    """check if we can reach the right/top of the grid from start"""
    stack = [start]
    blocked.remove(start)  # mark as visited
    while stack:
        r, c = stack.pop()
        if r == 1 or c == C:
            return True
        for dr, dc in dir:
            nr, nc = r + dr, c + dc
            if (nr, nc) in blocked:
                stack.append((nr, nc))
                blocked.remove((nr, nc))
    return False


for wall in blocked.copy():
    if wall in blocked and (wall[1] == 1 or wall[0] == R):  # start search if the wall is on the left/bottom of the grid
        if dfs(wall):
            print("NO")
            sys.exit()

print("YES")
