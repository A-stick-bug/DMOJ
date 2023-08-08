# reword problem: given the InOrder traversal of a full binary tree, print the tree (layer by layer)
# note: each node has either 0 or 2 children
# using recursion: take middle and cut into 2, base case is only having 2 nodes remaining

# example:
# 1 6 4 3 5 2 7    -- depth
#       3          -- 1
#   6       2      -- 2
# 1   4   5   7    -- 3

n = int(input())  # depth of tree/number of layers
in_order = list(map(int, input().split()))

tree = [[] for _ in range(n)]


def generate(start, end, layer):  # note: the layer can also be calculated using log and (end - start)
    if layer == n:  # base case: reached last layer
        tree[layer-1].append(in_order[start])
        return

    mid = (end + start) // 2
    tree[layer-1].append(in_order[mid])  # -1 because 'tree' uses 0-indexing and the layers use 1-indexing
    generate(start, mid - 1, layer + 1)  # do left side, then right
    generate(mid + 1, end, layer + 1)


generate(0, len(in_order) - 1, 1)

for row in tree:
    print(*row)
