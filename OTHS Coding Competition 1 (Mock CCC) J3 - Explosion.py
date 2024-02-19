# solution 2: using loops and conditions

N, D = map(int, input().split())
arr = list(map(int, input().split()))

groups = largest = 1
prev = arr[0]
cur = 1

for i in arr[1:]:
    if abs(prev - i) <= D:
        cur += 1
    else:
        groups += 1
        cur = 1

    largest = max(largest, cur)
    prev = i

print(groups)
print(largest)

# # solution 1: using disjoint set
# # items in the same group will all explode if one bomb in the group explodes
#
#
# class DisjointSet:
#     def __init__(self, N):
#         self.parent = [i for i in range(N + 1)]  # disjoint set stuff
#         self.size = [1] * (N + 1)
#
#     def find(self, node):
#         if self.parent[node] != node:  # go up until we reach the root
#             # attach everything on our way to the root (path compression)
#             self.parent[node] = self.find(self.parent[node])
#         return self.parent[node]
#
#     def union(self, a, b):
#         root_a = self.find(a)
#         root_b = self.find(b)
#         if root_a == root_b:
#             return
#         if self.size[root_b] > self.size[root_a]:  # join the smaller to the larger
#             root_a, root_b = root_b, root_a  # swap
#         self.parent[root_b] = root_a
#         self.size[root_a] += self.size[root_b]
#
#
# N, D = map(int, input().split())
# arr = list(map(int, input().split()))
#
# ds = DisjointSet(N)
# for i in range(N - 1):
#     if abs(arr[i] - arr[i + 1]) <= D:
#         ds.union(i, i + 1)
#
# roots = set()
# for i in range(N):
#     roots.add(ds.find(i))
#
# print(len(roots))
# print(max(ds.size))
