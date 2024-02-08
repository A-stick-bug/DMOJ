import sys

input = sys.stdin.readline


def solve(c):
    def factor(n):
        """prime factorize a number"""
        i = 2
        fac = []
        while i * i <= n:
            if n % i:
                i += 1
            else:
                n //= i
                fac.append(i)
        if n > 1:
            fac.append(n)
        return fac

    factors = factor(c)
    pow = {}
    for f in factors:  # find the powers of each prime factor
        if f in pow:
            pow[f] += 1
        else:
            pow[f] = 1
    total = 1
    for p in pow.values():
        total *= (p * 2 + 1)
    return total


for _ in range(int(input())):
    n = int(input())
    print(solve(n))
