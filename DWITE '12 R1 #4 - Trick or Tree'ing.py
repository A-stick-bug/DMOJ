import sys

sys.setrecursionlimit(100000)
MN = 1000
inf = 1 << 30


def solve():
    def add_edge(a, b):
        graph[a].append(b)
        graph[b].append(a)

    def print_edge_list(graph):
        """given a graph, print its edges"""
        for i in range(len(graph)):
            for j in graph[i]:
                if i < j:
                    print(i, j)

    def find_next_end(start):
        for i in range(start, len(s)):
            if s[i] in ") ":
                return i
        return len(s)

    s = input()
    idx = 0
    graph = [[] for _ in range(MN * 2)]
    node_idx = 0
    n = 0  # node count
    total = 0

    # turn into tree
    stack = []
    while idx < len(s):
        # print(idx, stack)
        if s[idx] == "(":  # start of group
            idx += 1
        elif s[idx] == " ":  # empty space?
            idx += 1
        elif s[idx] == ")":  # end group
            a = stack.pop()
            b = stack.pop()
            add_edge(a, node_idx)
            add_edge(b, node_idx)
            stack.append(node_idx)
            node_idx += 1
            idx += 1

        else:  # number
            nxt_idx = find_next_end(idx)
            num = int(s[idx:nxt_idx])
            total += num
            stack.append(node_idx)
            node_idx += 1
            idx = nxt_idx

    def dfs(cur, prev):
        d = 0
        for adj in graph[cur]:
            if adj == prev:
                continue
            d = max(d, dfs(adj, cur) + 1)
        return d

    # print_edge_list(graph)
    print(2 * node_idx - 2 - dfs(node_idx - 1, -1), total)


t = 5
for _ in range(t):
    solve()
