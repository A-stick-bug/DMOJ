# TLE, PYTHON IS TOO SLOW, CHECK C++ CODE
#
# https://dmoj.ca/problem/coci12c6p3
# Observations: N < 5000 -> strict N^2
# What can we do in N^2?
# - 3sum, a simple solution to 3sum is putting all pairs (i,j) in a dict {value:[(i1,j2), (i2, j2)]}, n^3 -> n^2
# - notice that we only need to check if a sum of pairs exists so a bool array will work

n = int(input())
arr = list(map(int, input().split()))

OFFSET = 200001
exists = [False] * OFFSET * 2
total = 0

for i in range(n):
    for j in range(i):  # 3-sum with numbers before current index
        if exists[OFFSET + arr[i] - arr[j]]:  # matched pair
            total += 1
            break
    for j in range(i + 1):  # current number can now be match with other numbers before it
        exists[OFFSET + arr[i] + arr[j]] = True

print(total)
