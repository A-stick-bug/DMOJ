# https://dmoj.ca/problem/oly24practice6
# Tree DP
# state: [current node][node's color]
# state contains: max/min number of red nodes in cur's subtree given cur's color

import sys

sys.setrecursionlimit(200000)
idx = -1


def make_tree(cur):
    global idx
    idx += 1
    if child[idx] == "0":
        return
    elif child[idx] == "1":
        graph[cur].append(idx + 1)
        make_tree(idx + 1)
    else:
        graph[cur].append(idx + 1)
        make_tree(idx + 1)
        graph[cur].append(idx + 1)
        make_tree(idx + 1)


def maximize(cur, color):
    if dp1[color][cur] != -1:
        return dp1[color][cur]
    choices = [0, 1, 2]
    choices.remove(color)
    if len(graph[cur]) == 2:
        a1, a2 = graph[cur]
        ans = (color == 0) + max(maximize(a1, choices[0]) + maximize(a2, choices[1]),
                                 maximize(a1, choices[1]) + maximize(a2, choices[0]))
    elif len(graph[cur]) == 1:
        a = graph[cur][0]
        ans = (color == 0) + max(maximize(a, choices[0]),
                                 maximize(a, choices[1]))
    else:
        ans = (color == 0)
    dp1[color][cur] = ans
    return dp1[color][cur]


def minimize(cur, color):
    if dp2[color][cur] != -1:
        return dp2[color][cur]
    choices = [0, 1, 2]
    choices.remove(color)
    if len(graph[cur]) == 2:
        a1, a2 = graph[cur]
        ans = (color == 0) + min(minimize(a1, choices[0]) + minimize(a2, choices[1]),
                                 minimize(a1, choices[1]) + minimize(a2, choices[0]))
    elif len(graph[cur]) == 1:
        a = graph[cur][0]
        ans = (color == 0) + min(minimize(a, choices[0]),
                                 minimize(a, choices[1]))
    else:
        ans = (color == 0)
    dp2[color][cur] = ans
    return dp2[color][cur]


child = input()
n = len(child)
graph = [[] for _ in range(n + 1)]
make_tree(0)

dp1 = [[-1] * n for _ in range(3)]
dp2 = [[-1] * n for _ in range(3)]
print(max(maximize(0, i) for i in range(3)),
      min(minimize(0, i) for i in range(3)))
