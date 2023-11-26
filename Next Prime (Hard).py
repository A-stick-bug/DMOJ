# just find some prime tests online lol
# first use fermat test to filter out easy to spot primes, then try miller-rabin test
# also use the built-in pow(base, exp, mod) to do b^x % m

import random
import sys


def fermat_prime(n, k=5):
    if n <= 1 or n == 4:
        return False
    if n <= 3:
        return True
    while k > 0:
        a = 2 + random.randint(1, n - 4)
        if pow(a, n - 1, n) != 1:
            return False
        k -= 1
    return True


def miller_prime(n, k=5):
    if n <= 1 or n == 4:
        return False
    if n <= 3:
        return True
    d = n - 1
    while d % 2 == 0:
        d //= 2
    for _ in range(k):
        a = 2 + random.randint(1, n - 4)
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        while d != n - 1:
            x = (x * x) % n
            d *= 2
            if x == 1:
                return False
            if x == n - 1:
                break
        else:
            return False
    return True


n = int(input())

if n <= 2:  # handle corner cases
    print(2)
    sys.exit()

# do odd numbers only to save some time (n|1 rounds up to nearest odd number)
for num in range(n | 1, 10 ** 8 + 10000, 2):
    if fermat_prime(num, 10000) and miller_prime(num, 10000):
        print(num)
        break
