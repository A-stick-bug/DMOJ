from collections import deque

n = int(input())
s = input()

res = deque([s[0]])
for char in s[1:]:
    if char <= res[0]:
        res.appendleft(char)
    else:
        res.append(char)

print(*res, sep="")
