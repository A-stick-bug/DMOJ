# https://dmoj.ca/problem/dmpg17s2
# template disjoint set problem, I used union by size because it is more intuitive

def find(node):
    if parent[node] != node:  # go up until we reach the root
        parent[node] = find(parent[node])  # attach everything on our way to the root (path compression)
    return parent[node]


def union(a, b):
    root_a = find(a)
    root_b = find(b)
    if size[root_b] > size[root_a]:  # join the smaller to the larger
        root_a, root_b = root_b, root_a  # swap
    parent[root_b] = root_a
    size[root_a] += size[root_b]


N, Q = map(int, input().split())

parent = [i for i in range(N + 1)]  # disjoint set stuff
size = [1] * (N + 1)

for _ in range(Q):
    q, x, y = input().split()
    x, y = int(x), int(y)
    if q == 'A':
        union(x, y)
    else:
        if find(x) == find(y):
            print("Y")
        else:
            print("N")
