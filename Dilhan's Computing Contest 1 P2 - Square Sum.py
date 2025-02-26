"""
https://dmoj.ca/problem/dcc1p2
Google a bunch of math formulas
Visualization used for example: https://www.desmos.com/calculator/q0ycnkjuqy
Split the sum into 3 pieces

let x = isqrt(A)
Chunk 1 (triangle): x+1 + (1 + 4 + 9 + ... + x^2) = x+1 + x*(x+1)*(2*x+1)//6

let y = isqrt(B) - isqrt(A)
Chunk 2 (parallelogram): y * (A + 1)

Chunk 3 (triangle): find quadratic function and sum over interval of integer coordinates

references:
- https://math.stackexchange.com/questions/680646/get-polynomial-function-from-3-points
- https://oeis.org/
- https://www.cuemath.com/sum-of-squares-formula/
"""

from math import isqrt

MOD = 998244353


def solve():
    A, B = map(int, input().split())
    if A > B:
        A, B = B, A

    total = 0

    # chunk 1
    x = isqrt(A)
    total += x + 1 + x * (x + 1) * (2 * x + 1) // 6

    # chunk 2
    y = isqrt(B) - isqrt(A)
    total += y * (A + 1)

    # chunk 3

    # first 3 points on quadratic
    cur = isqrt(A + B)
    f = [None]  # 1-indexed
    for i in range(3):
        f.append(1 + (A - (cur * cur - B)))
        cur -= 1

    # f(x) = ax^2 + bx + c
    a = -1
    b = (f[2] - f[1]) // (2 - 1) - a * (1 + 2)
    c = f[1] - a * 1 ** 2 - b * 1

    # def func(x_val):
    #     return a * x_val ** 2 + b * x_val + c

    h = isqrt(A + B) - isqrt(B)

    # sum of f(i) for i in [1, h]
    total += a * h * (h + 1) * (2 * h + 1) // 6  # quadratic part
    total += b * (h * (h + 1) // 2)  # linear part
    total += c * h  # constant part

    print(total % MOD)


for _ in range(int(input())):
    solve()
