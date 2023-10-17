from collections import Counter
import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
freq = Counter(arr)
total = sum(arr)

inflation = 0
for _ in range(int(input())):  # handle queries
    q = input().split()
    if q[0] == "INFLATION":
        more_inflation = int(q[1])
        inflation += more_inflation
        total += n * more_inflation

    else:
        x, y = map(int, q[1:])  # turn all x into y
        if x == y:  # setting to same value doesn't do anything, we just skip
            print(total)
            continue

        x -= inflation  # don't care about inflation when keep count of how many of each value there is
        y -= inflation
        total += ((y - x) * freq[x])

        x_count = freq[x]
        freq[y] += x_count
        freq[x] = 0

    print(total)
