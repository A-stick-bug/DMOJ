# sanity check, try trivial 10/100 solution


T, N = map(int, input().split())
if T == 1:
    print(N - 1)
    for i in range(N - 1):
        idx = int(input())
        print(i + 1)

else:
    arr = list(map(int, input().split()))
    from collections import Counter

    f = Counter(arr)
    dup = [k for k in f if f[k] == 2]
    assert len(dup) == 1

    indices = [i for i in range(N) if arr[i] == dup[0]]
    print(*indices)

# [2 3 1 3]
# import random
#
# seed = 1434
# K = 100_000
#
# T, N = map(int, input().split())
#
# arr = [random.randint(1, K) for _ in range(N)]
# for _ in range(N):
#     idx = int(input())
#     print(arr[idx])
#
#
