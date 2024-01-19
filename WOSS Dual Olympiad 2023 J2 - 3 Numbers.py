from itertools import permutations

res = -10000000000
arr = list(map(int, input().split()))
for perm in permutations(arr):
    print(perm)
    res = max(res,
              perm[0]+perm[1]+perm[2],
              perm[0]*perm[1]+perm[2],
              perm[0]*(perm[1]+perm[2]),
              perm[0]+perm[1]*perm[2],
              perm[0]*perm[1]*perm[2])

print(res)
