# https://dmoj.ca/problem/coci15c1p3
# kind of like DP
# maintain frequency list, use existing previous value if possible at each index

n = int(input())
arr = list(map(int, input().split()))
MN = max(arr)

total = 0
freq = [0] * (MN + 2)
for i in range(n):
    if freq[arr[i] + 1] > 0:  # transition from existing value
        freq[arr[i] + 1] -= 1
        freq[arr[i]] += 1
    else:  # no existing value, start new one
        total += 1
        freq[arr[i]] += 1

print(total)
