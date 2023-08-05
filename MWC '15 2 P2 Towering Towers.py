# monotonic stack with ascending order

n = int(input())
towers = list(map(int, input().split()))
stack = [(towers[0], 0)]  # (height of current tower, how many towers you can see beyond this)
res = [0]  # first tower is an exception because you can't see any other towers

for tower in towers[1:]:
    popped = 1
    while stack:
        if tower >= stack[-1][0]:  # we can see beyond the previous tower
            # if you are higher than this tower, you can see everything beyond it with equal or lower height as well
            popped += stack.pop()[1]
        else:
            break

    res.append(popped)
    # store the height of the tower and how many towers before this one has a lower height
    stack.append((tower, popped))

print(*res)
