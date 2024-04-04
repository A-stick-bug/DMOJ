# https://dmoj.ca/problem/wacreject4
# notice that the data is randomly  generated
# this means that if we just get the values at random indices, we will very likely get 2
# indices with the same value after 10000 guesses (this is basically the birthday paradox)

n = int(input())
MN = 10000
a1 = [-1] * (n + 1)
a2 = [-1] * (n + 1)

for i in range(MN):
    print(i + 1, i + 1)  # 1-indexed
    a, b = map(int, input().split())

    if a == b:  # found answer early
        break
    if a1[b] != -1:
        print(a1[b], i + 1)
        break
    elif a2[a] != -1:
        print(i + 1, a2[a])
        break

    a1[a] = i + 1
    a2[b] = i + 1
