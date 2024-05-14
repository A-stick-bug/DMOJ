def change_base(n, base):
    res = []
    while n != 0:
        res.append(n % base)
        n //= base
    return "".join(map(str, reversed(res)))


for _ in range(5):
    n1, b1 = map(int, input().split())
    n2, b2 = map(int, input().split())

    n1, n2 = int(str(n1), b1), int(str(n2), b2)
    print(change_base(n1 * n2, int(input())))
