# https://dmoj.ca/problem/segmentgame
# Good practice problem to do before you learn segment trees
# - First fill in the tree using values we know for sure
# - If we know node i and not its children, make the children as small as possible (greedy)

import sys

n = int(input())
seg = [-1] + list(map(lambda x: -1 if x == "x" else int(x), input().split()))

for i in reversed(range(1, n)):  # fill in values we know for sure
    if seg[i * 2] != -1 and seg[i * 2 + 1] != -1:
        seg[i] = min(seg[i * 2], seg[i * 2 + 1])

if seg[1] == -1:  # root can be anything means we can just put -inf for all `x`
    print("Negative infinity!")
    sys.exit()

for i in range(1, n):
    # push down the smallest value possible
    if seg[i * 2] == -1:
        seg[i * 2] = seg[i]
    if seg[i * 2 + 1] == -1:
        seg[i * 2 + 1] = seg[i]

print(sum(seg[1:]))

# def print_tree():
#     print("\n".join(
#         " ".join(
#             map(str, [seg[j] for j in range(2 ** i, 2 * 2 ** i)])).center(50)
#         for i in range(n.bit_length())))
#
# print_tree()
# print(seg)
