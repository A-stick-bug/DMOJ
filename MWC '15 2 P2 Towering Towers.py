# https://dmoj.ca/problem/mwc15c2p2
# monotonic stack with strictly decreasing order
# previous greater element problem

# solution based on previous greater template
n = int(input())
towers = list(map(int, input().split()))

stack = []  # store the indices in the stack
res = [0] * n

for i in range(n):

    # pop all smaller elements in stack, remaining element is the previous greater element
    while stack and towers[i] >= towers[stack[-1]]:
        stack.pop()

    res[i] = i if not stack else i - stack[-1]  # get visible towers based on the index of the previous greater element
    stack.append(i)

print(*res)

# # my original solution without much knowledge on monotonic stacks
# n = int(input())
# towers = list(map(int, input().split()))
# stack = [(towers[0], 0)]  # (height of current tower, how many towers you can see beyond this)
# res = [0]  # first tower is an exception because you can't see any other towers
#
# for tower in towers[1:]:
#     popped = 1
#     while stack and tower >= stack[-1][0]:
#         # if you are higher than this tower, you can see everything beyond it with equal or lower height as well
#         popped += stack.pop()[1]
#
#     res.append(popped)
#     # store the height of the tower and how many towers before this one has a lower height
#     stack.append((tower, popped))
#
# print(*res)
