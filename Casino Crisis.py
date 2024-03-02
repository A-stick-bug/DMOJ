# https://dmoj.ca/problem/casinocrisis
# not sure how this passes until the query limit but basically for every number
# keep on trying to move it to its position, go from small to large numbers


def update_range(l, r):
    """simulates swapping the numbers in the range [l, r]"""
    if l == r:
        return
    moves.append((l, r))
    sub = arr[l:r + 1]
    le = r - l + 1
    s = sorted(sub)
    pos = {}
    for i, v in enumerate(sub):
        pos[v] = i
    for i in range(len(sub) // 2):
        small = pos[s[i]]
        large = pos[s[le - i - 1]]
        arr[l + small], arr[l + large] = arr[l + large], arr[l + small]


n, _ = map(int, input().split())
arr = list(map(int, input().split()))
moves = []

for i in range(n):
    while arr[i] != i + 1:  # keep on moving to the front until it's where it belongs
        update_range(i, arr.index(i + 1))
    # print(arr)

print(len(moves))
for l, r in moves:
    print(l + 1, r + 1)
