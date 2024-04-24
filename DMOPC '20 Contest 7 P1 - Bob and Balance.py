# first sort the array and pair element i with element i+n

import sys

print = sys.stdout.write

n = int(input())
arr = list(map(int, input().split()))
arr = list(enumerate(arr))
arr.sort(key=lambda x: x[1])  # sort by value

total = 0
res = []
for i in range(n):
    total += arr[i][1] != arr[i + n][1]
    res.append((arr[i][0], arr[i + n][0]))

print(str(total) + "\n")
for i in res:
    print(" ".join(map(lambda x: str(x + 1), i)) + "\n")
