# https://dmoj.ca/problem/rgpc18p3
# using a difference array and sliding window

n, t = map(int, input().split())

fills = [0] * (n + 1)  # difference array
for _ in range(t):
    start, end, amt = map(int, input().split())
    fills[start - 1] += amt  # turn into 0 indexing
    fills[end] -= amt

choco = []  # amount of chocolate in each cup
cur = 0
for i in range(n):
    cur += fills[i]
    choco.append(cur)

limit = int(input())  # use sliding window and find maximum window length
left = total = res = 0
for right in range(n):
    total += choco[right]
    while total > limit:  # move left pointer until we are under the limit
        total -= choco[left]
        left += 1

    res = max(res, right - left + 1)  # update max window length

print(res)
