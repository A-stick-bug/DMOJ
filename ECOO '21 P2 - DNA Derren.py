# https://dmoj.ca/problem/ecoo21p2
# simple greedy

s = input()
n = len(s)

res = []
stack = []
for i in s:
    if stack and ((i == "A" and stack[-1] != "A") or (i != "A" and stack[-1] == "A")):
        stack.append(i)
    else:
        if stack:
            res.append("".join(stack))
        stack.clear()
        stack.append(i)

res.append("".join(stack))  # add leftovers
print(*res)
