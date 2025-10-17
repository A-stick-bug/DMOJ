# https://dmoj.ca/problem/dmopc21c1p3
# We make the graph acyclic by making all edges go from the smaller node number to the larger one
# - lay the nodes out in a line and you can see it is indeed acyclic
#
# The intuition used is very similar to centroid decomposition on a tree
# - By splitting the set of nodes in half and recursing, we are guaranteed to cover all edges
# - We also know that each node is used log(n) times, fitting within the required limit of 3000
#
# Time complexity analysis
# T(n) = 2T(n/2) + O(n^2)
# T(n) = O(n^2), by the master theorem

n, m = map(int, input().split())
edges = [tuple(sorted(map(int, input().split()))) for _ in range(m)]
mp = {v: i + 1 for i, v in enumerate(edges)}
nodes = list(range(1, n + 1))

flip = [0] * (m + 1)  # 1-indexed


def ask(A, B):
    print(f"? {len(A)} {len(B)}")
    print(*A)
    print(*B)
    res = list(map(int, input().split()))
    return res[1:]


def solve(cur):
    if len(cur) < 2:
        return
    le_split = len(cur) // 2
    A = cur[:le_split]  # note: max(A) < min(B)
    B = cur[le_split:]
    edge_idx = set(ask(A, B))  # edges that go `a` to `b`, where `a` < `b`
    for a in A:
        for b in B:
            if (a, b) not in mp:  # no edge from a to b, ignore
                continue
            e = mp[(a, b)]
            # the current edge goes from b to a, we flip so that all edges go from smaller to larger node
            if e not in edge_idx:
                flip[e] = 1

    solve(A)
    solve(B)


solve(nodes)
print(f"! {''.join(map(str, flip[1:]))}")
