# https://dmoj.ca/problem/gcj18qrb
# observation: t-sort is just sorting all odd indices and then sort all even indices (as odd/even are never swapped)
# we just simulate this by separating the odd and even indices, sorting them, and merging them together
# now we just check for the first incorrect element, if any

def solve():
    inf = 10000000000000000000000000
    n = int(input())
    arr = list(map(int, input().split())) + [inf, inf, inf]  # add padding to handle edge case

    odd = []  # sort odd and even separately
    even = []
    for i in range(0, n, 2):
        odd.append(arr[i])
        even.append(arr[i + 1])
    odd.sort()
    even.sort()

    res = []  # merge odd and even together
    for i, j in zip(odd, even):
        res.append(i)
        res.append(j)
    while res[-1] == inf:  # remove padding
        res.pop()

    for i, (a, b) in enumerate(zip(res, sorted(res))):  # check for different indices
        if a != b:
            print(i)
            return

    print("OK")


for t in range(int(input())):
    print(f"Case #{t + 1}: ", end="")
    solve()
