# number bases manipulation
# to represent a number as a distinct powers of 3, we must get rid of 2s in base 3
# after removing a 2, to minimize, turn everything after it into 0, to maximize turn everything after it into 1

pow3 = [3 ** i for i in reversed(range(39))]


def base3(n: int):
    res = [0] * 39
    i = 0
    while n > 0:
        if n >= pow3[i]:
            res[i] += 1
            n -= pow3[i]
        else:
            i += 1
    return res


q = int(input())

for _ in range(q):
    l, r = map(int, input().split())
    l3 = base3(l)
    r3 = base3(r)

    for i in range(len(r3)):  # r3 <= r, maximize r3
        if r3[i] == 2:
            for j in range(i,len(r3)):
                r3[j] = 1
            break

    for i in reversed(range(len(l3))):  # l3 >= l, minimize l3
        if l3[i] >= 2:
            for j in range(i, len(l3)):
                l3[j] = 0
            l3[i - 1] += 1

    # base 2
    print(int("".join(map(str, r3)), 2) - int("".join(map(str, l3)), 2) + 1)
