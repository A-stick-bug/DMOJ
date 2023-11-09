from functools import reduce

n = int(input())
arr = list(map(int, input().split()))

if n < 14:  # brute force handles corner cases
    res = 1
    l = r = 0
    for i in range(n):
        for j in range(i, n):
            p = reduce(lambda a, b: a * b, arr[i:j + 1]) / (j - i + 1)
            if p > res:
                res = p
                l = i
                r = j
    print(l + 1, r + 1)

else:  # use normal logic
    if arr[0] == 1:
        print(2, n)
    elif arr[-1] == 1:
        print(1, n-1)
    else:
        print(1, n)