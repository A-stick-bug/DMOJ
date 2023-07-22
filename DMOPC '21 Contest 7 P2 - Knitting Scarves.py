# submit in PYPY3 or else TLE
# very weird graph theory
# oops, it's actually supposed to be a doubly linked list

nodes, steps = map(int, input().split())

# +2 because on the left, 0 will act as a pointer to the root node and also prevent out of bounds
# on the right, the element is just there so that when we move the last element, it doesn't go out of bounds
before = [i - 1 for i in range(nodes + 2)]
next = [i + 1 for i in range(nodes + 2)]

for i in range(steps):
    start, end, cut = map(int, input().split())

    # fill in the gap
    previous = before[start]  # node before start
    next[previous] = next[end]  # make it point to the node after end (filling the gap after removing the segment)
    after_end = next[end]  # node after end
    before[after_end] = previous  # fixing the gap

    # fix connection after insertion
    temp = next[cut]
    before[temp] = end
    next[end] = temp

    next[cut] = start
    before[start] = cut

i = 0  # whatever 0 points to will be the root/head/start node
res = []
for _ in range(nodes):
    i = next[i]
    res.append(str(i))
print(*res, sep=" ")

# # bad code that almost TLE and MLE and only works in PYPY3
#
# def print_graph():
#     i = 0  # whatever 0 points to will be the root/head/start node
#     res = []
#     for _ in range(n):
#         i = graph[i][1]
#         res.append(str(i))
#     return " ".join(res)
#
#
# n, steps = map(int, input().split())
# graph = [[i - 1, i + 1] for i in range(n + 2)]
#
# for i in range(steps):
#     start, end, cut = map(int, input().split())
#
#     # fill in the gap
#     prev = graph[start][0]
#     graph[prev][1] = graph[end][1]
#     next = graph[end][1]
#     graph[next][0] = graph[start][0]
#
#     # fix connection after insertion
#     next = graph[cut][1]
#     graph[next][0] = end
#     graph[end][1] = next
#
#     graph[cut][1] = start
#     graph[start][0] = cut
#
# print(print_graph())
