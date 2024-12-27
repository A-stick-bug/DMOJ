# https://dmoj.ca/problem/aac3p4
# ad hoc with observations

from collections import Counter

N, M = map(int, input().split())
rows = list(map(int, input().split()))
cols = list(map(int, input().split()))

rows = Counter([rows[i] - i for i in range(N) if rows[i] != -1])  # add time to reach the row
cols = Counter([cols[i] - i for i in range(M) if cols[i] != -1])  # add time to reach the col

print(sum((rows & cols).values()))
