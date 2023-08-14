# https://dmoj.ca/problem/alexquiz2
# using the Sieve of Eratosthenes for efficiency (n * log(log(n))), using the  n*sqrt(n) method may also work
# use a prefix sum array for O(1) per query

import sys

input = sys.stdin.readline
num = 100_001

prime = [True for i in range(num + 1)]
p = 2
while p * p <= num:
    if prime[p]:
        for i in range(p * p, num + 1, p):
            prime[i] = False
    p += 1

# turn into prefix sum array
prime[0] = 0
prime[1] = 0
for i in range(2, num + 1):
    if prime[i]:
        prime[i] = i+prime[i-1]
    else:
        prime[i] = prime[i-1]

# total of Q queries
for _ in range(int(input())):
    a, b = map(int, input().split())
    print(prime[b] - prime[a - 1])
