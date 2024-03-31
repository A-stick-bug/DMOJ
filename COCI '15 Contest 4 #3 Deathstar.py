# https://dmoj.ca/problem/coci15c4p3
# straightforwards ad hoc constructive with bitwise operations

n = int(input())
res = [0] * n

for i in range(n):
    and_val = list(map(int, input().split()))
    for j in range(n):
        res[i] |= and_val[j]

print(*res)
