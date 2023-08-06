import sys

input = sys.stdin.readline

n_stations = int(input())
min_troops = int(input())
n_waves = int(input())

add_troops = [0 for _ in range(n_stations+2)]

for _ in range(n_waves):
    start, end, amount = map(int, input().split())
    add_troops[start] += amount
    add_troops[end+1] -= amount

res = 0
troops = 0
for i in range(1,n_stations+1):
    troops += add_troops[i]
    # print(troops)
    if troops < min_troops:
        res += 1

print(res)
