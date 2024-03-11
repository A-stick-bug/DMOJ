# try 2 strategies: move the big pig to the back and move the small pig to the start

N, L = map(int, input().split())
arr = list(map(int, input().split()))


def solve1():
    # we can remove one and then try to fit as many as possible in order
    skip = False
    total = 0
    for i in range(N):
        if total + arr[i] > L:
            if skip:
                return i - skip
            else:
                skip = True
                total -= max(arr[:i + 1])

        total += arr[i]

    return N - skip


def solve2():
    total = 0
    for i in range(N):
        if total + arr[i] > L:
            return i + ((L - total) >= min(arr[i:]))
        total += arr[i]
    return N


a, b = solve1(), solve2()
print(max(a, b))
