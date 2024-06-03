# https://dmoj.ca/problem/chores
# simple greedy, always do chores that take less time to finish first since they are counted the most
# use some math to keep track of the total time

MOD = 10 ** 9 + 7
n = int(input())
chores = [tuple(map(int, input().split())) for _ in range(n)]
chores.sort(key=lambda x: x[0])  # sort by time

total = 0
height = 0
for time, cnt in chores:
    total += height * cnt + time * cnt * (cnt + 1) // 2
    height += cnt * time
print(total % MOD)
