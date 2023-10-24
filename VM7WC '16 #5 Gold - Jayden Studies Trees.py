# https://dmoj.ca/problem/vmss7wc16c5p3
# finding the diameter (longest path) in a tree
#
# for each node, the longest path either goes through the longest branch below it or
# we can consider the current node the 'root' and get the sum of the longest and second-longest path below

import sys

input = sys.stdin.readline
sys.setrecursionlimit(10000)

n = int(input())
tree = [[] for _ in range(n + 1)]  # create tree from input
for _ in range(n - 1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)


def solve(cur, prev):
    global res
    longest = 0
    second_longest = 0
    for adj in tree[cur]:  # check each branch below
        if adj == prev:  # avoid infinite loop
            continue

        branch = solve(adj, cur) + 1  # branch depth
        if branch >= longest:  # update longest and second longest depths
            second_longest = longest
            longest = branch
        elif branch > second_longest:
            second_longest = branch

    res = max(res, longest + second_longest)  # check distance if we consider the current node the root
    return longest


res = 0
solve(1, 0)  # root tree at 1
print(res)
