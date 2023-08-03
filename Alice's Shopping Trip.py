time, n = map(int, input().split())
stores = [int(input()) for _ in range(n)]
stores.sort(key=lambda x: abs(x))

res = 0  # number of stores visited
cur = 0  # current location

for loc in stores:
    dist = abs(cur - loc)  # distance from current location to next
    if time - dist < 0:  # check if we are out of time
        break

    cur = loc  # update to new location
    time -= dist
    res += 1

print(res)

# test case:
# 25 5
# 10
# -3
# 8
# -7
# 1

# answer: 4
