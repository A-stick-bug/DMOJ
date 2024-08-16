# https://dmoj.ca/problem/dmopc22c3p1

n, m = sorted(map(int, input().split()), reverse=True)  # N >= M

if n % 2 == 0 or m % 2 == 0:
    r = g = n * m // 2
else:
    total = n * m
    r = (n + 1) // 2 * m
    g = total - r

print(r, g)
