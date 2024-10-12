# https://dmoj.ca/problem/othscc2p3
# Simple math with logic
# It is optimal to click the second button (+1111) as many times as you can
# without exceeding the number we are trying to reach, then use the first button (+1)

n = int(input())

moves = 0
cur = 0
while cur + 1111 <= n:  # use second button
    cur += 1111
    moves += 1

while cur + 1 <= n:  # use first button
    cur += 1
    moves += 1

print(moves)
