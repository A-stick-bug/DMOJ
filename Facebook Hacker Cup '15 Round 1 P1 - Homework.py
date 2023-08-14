# https://dmoj.ca/problem/fhc15c1p1

num = 10_000_001

prime = [0 for i in range(num + 1)]  # precompute primes using a sieve
p = 2
while p <= num:
    if prime[p] == 0:  # this number is prime
        for i in range(p, num + 1, p):
            prime[i] += 1
    p += 1

for i in range(1, int(input()) + 1):  # for each test case
    a, b, k = map(int, input().split())
    res = 0
    for n in range(a, b + 1):
        if prime[n] == k:
            res += 1

    print(f"Case #{i}: {res}")
