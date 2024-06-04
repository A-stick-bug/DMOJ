"""
https://dmoj.ca/problem/cpc21c1p2
Go read editorial, question is very unintuitive
"""

n = int(input()) * 2 + 1
a = list(map(int, input().split()))
b = list(map(int, input().split()))

ans = 0
for i in a + b:
    ans ^= i

a = list(map(lambda x: x ^ ans, a))
if sorted(a) == sorted(b):
    print(ans)
else:
    print(-1)
