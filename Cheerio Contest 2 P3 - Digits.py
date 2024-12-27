# https://dmoj.ca/problem/cheerio2p3
# just observe the first few terms to get the pattern
# check commented code below

X, Y, Q = map(int, input().split())
X, Y = min(X, Y), max(X, Y)

for _ in range(Q):
    idx = int(input())
    if idx == X:
        print(8)
    elif idx == X + Y:
        print(1)
    elif idx <= Y:
        print(9)
    else:
        print(0)

# # observations made with this
# for s in range(1, 6):
#     for t in range(s, 6):
#         print(s, t, int('9'*s) * int('9'*t))
