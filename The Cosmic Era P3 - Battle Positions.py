# https://dmoj.ca/problem/seed3

import sys

input = sys.stdin.readline
n_stations = int(input())
min_troops = int(input())
n_waves = int(input())

add_troops = [0 for _ in range(n_stations + 2)]  # +2 for 1-indexing and preventing index out of bounds

for _ in range(n_waves):
    start, end, amount = map(int, input().split())
    add_troops[start] += amount  # +amount troops for stations up to end
    add_troops[end + 1] -= amount  # once we are out of this wave, the troops will not be added anymore

res = 0
troops = 0  # how many troops are in the current station
for i in range(1, n_stations + 1):
    troops += add_troops[i]  # update the amount of troops at this station
    # print(troops)
    if troops < min_troops:
        res += 1

print(res)
