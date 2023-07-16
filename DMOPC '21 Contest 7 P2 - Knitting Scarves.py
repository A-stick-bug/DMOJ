# very weird graph theory
# oops, it's actually supposed to be a doubly linked list

def print_graph():
    i = 0  # whatever 0 points to will be the root/head/start node
    res = []
    for _ in range(n):
        i = graph[i][1]
        res.append(str(i))
    return " ".join(res)


n, steps = map(int, input().split())
graph = [[i - 1, i + 1] for i in range(n + 2)]

for i in range(steps):
    start, end, cut = map(int, input().split())

    # fill in the gap
    prev = graph[start][0]
    graph[prev][1] = graph[end][1]  # 3: 2, 6
    next = graph[end][1]
    graph[next][0] = graph[start][0]

    # fix connection after insertion
    next = graph[cut][1]
    graph[next][0] = end
    graph[end][1] = next

    graph[cut][1] = start
    graph[start][0] = cut

print(print_graph())
