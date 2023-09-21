"""
https://dmoj.ca/problem/tropical

Use 2 difference arrays:
- for operation 0, we turn the 1-indexed queries into 0-indexed ones and update the difference array normally
  (extra cell at the end to prevent index out of bounds)
- for operation 1, we use a reversed difference array and queries can stay 1-indexed
  (extra cell at the start)

Change the psa method when converting diff to regular array
- Instead of having 'constant' updates, we have 'linear' ones

"""

n, q = map(int, input().split())
diff = [[0, 0] for _ in range(n + 1)]  # [start value, difference after every cell (slope?)]
diff2 = [[0, 0] for _ in range(n + 1)]

for _ in range(q):
    x, l, r, a, b = map(int, input().split())

    if x == 0:
        l -= 1  # turn into 0-indexing
        r -= 1
        diff[l][0] += a
        diff[l][1] += b
        diff[r + 1][0] -= a + b * (r - l + 1)
        diff[r + 1][1] -= b

    else:  # shifted 1 to the right (1-indexed)
        diff2[l - 1][0] -= a + b * (r - l + 1)
        diff2[l - 1][1] -= b
        diff2[r][0] += a
        diff2[r][1] += b

diff.pop()  # last element is useless, it's there to prevent index out of bounds

# use the first difference array normally, considering the 'slope' (change for every cell)
arr = [0] * n
first = second = 0
for i, (d1, d2) in enumerate(diff):
    first += d1
    second += d2
    first += second
    arr[i] = first

# iterate second array in reverse
first = second = 0
for i in reversed(range(n)):
    first += diff2[i + 1][0]  # second diff is 1-indexed, ignore first element
    second += diff2[i + 1][1]
    first += second
    arr[i] += first

for i in arr:
    print(i)
