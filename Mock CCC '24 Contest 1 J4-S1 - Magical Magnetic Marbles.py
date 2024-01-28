import sys

n,m = map(int, input().split())
arr = list(map(int, list(input())))

# perform automatic merge
for i in range(1, len(arr)):
    if arr[i] == 1 and arr[i-1] == 1:
        arr[i-1] = 0

arr = list(map(int, "".join(map(str, arr)).strip("0")))

if not arr and m == 0:
    print(0)
    sys.exit()
if not arr:
    print(1)
    sys.exit()

prev = 1
prev1 = 0
dist = []

for i in range(1, len(arr)):
    if arr[i] == 1 and prev == 0:
        dist.append(i - prev1 - 1)
        prev1 = i

    prev = arr[i]


dist.sort()
total = len(dist) + 1
rem = 0

while rem < len(dist) and m >= dist[rem]:
    m -= dist[rem]
    rem += 1

print(total - rem)
