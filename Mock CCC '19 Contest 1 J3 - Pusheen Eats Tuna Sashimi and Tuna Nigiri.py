# https://dmoj.ca/problem/nccc6j3
# simple math question


def exists():
    i = 0
    while c - a * i >= 0:
        if (c - a * i) % b == 0:
            return True
        i += 1
    return False


for _ in range(int(input())):
    a, b, c = map(int, input().split())
    if exists():
        print("YES")
    else:
        print("NO")
