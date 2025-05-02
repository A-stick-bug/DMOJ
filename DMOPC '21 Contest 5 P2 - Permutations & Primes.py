# https://dmoj.ca/problem/dmopc21c5p2
# Observation based question
# Note that the sum of the first N numbers is N*(N+1)/2
# One of N and N+1 is even, so you end up with a product of 2 integers
# Thus it can't be prime
# Note: hardcode the small cases since this doesn't apply if N/2=1 or (N+1)/2=1

n = int(input())
if n == 1:
    print(1)
elif n == 2:
    print(-1)
else:
    thing = [1, 3, 2] + list(range(4, 10 ** 6 + 1))
    print(" ".join(map(str, thing[:n])))

# # Observe pattern below:
# from itertools import permutations
# from sympy import isprime
#
# for n in range(1, 100):
#     print(f"for {n}")
#     for perm in permutations(list(range(1, n+1))):
#         cur = 0
#         work=True
#         for i in perm:
#             cur += i
#             if isprime(cur):
#                 work =False
#                 break
#         if work:
#             print(perm)
#
