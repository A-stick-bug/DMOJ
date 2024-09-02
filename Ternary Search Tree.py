# https://dmoj.ca/problem/ternarysearchtree
# the tree is just a binary search tree with duplicate keys grouped together
# therefore, we can simply ignore duplicate values since their parent is always the same number

n = int(input())

get_default = lambda: [None, None]
root = int(input())
childs = {root: get_default()}

for _ in range(n - 1):
    node = int(input())
    cur = root

    if node in childs:
        print(node)
        continue

    while True:
        if node < cur:
            if childs[cur][0] is None:
                print(cur)
                childs[cur][0] = node
                childs[node] = get_default()
                break
            else:
                cur = childs[cur][0]
        elif node > cur:
            if childs[cur][1] is None:
                print(cur)
                childs[cur][1] = node
                childs[node] = get_default()
                break
            else:
                cur = childs[cur][1]
