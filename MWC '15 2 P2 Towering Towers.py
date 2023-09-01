# https://dmoj.ca/problem/mwc15c2p2
# monotonic stack with strictly decreasing order
# previous greater element problem

n = int(input())
towers = list(map(int, input().split()))
stack = [(towers[0], 0)]  # (height of current tower, how many towers you can see beyond this)
res = [0]  # first tower is an exception because you can't see any other towers

for tower in towers[1:]:
    popped = 1
    while stack and tower >= stack[-1][0]:
        # if you are higher than this tower, you can see everything beyond it with equal or lower height as well
        popped += stack.pop()[1]

    res.append(popped)
    # store the height of the tower and how many towers before this one has a lower height
    stack.append((tower, popped))

print(*res)


# similar solution
# n = int(input())
# towers = list(map(int, input().split()))
#
# stack = []  # store the indices in the stack
# res = [0] * n
#
# for i in range(1, n):  # first tower is an exception because it can never see any other towers
#     can_see = 1
#
#     # update towers with a lower height than current
#     while stack and towers[i] >= towers[stack[-1]]:
#         prev = stack.pop()
#         can_see += res[prev]
#
#     res[i] = can_see
#     stack.append(i)
#
# print(*res)

