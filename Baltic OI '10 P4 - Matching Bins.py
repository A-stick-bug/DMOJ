def is_greater(f1, f2):
    j = 0
    for i in range(m + 1):
        while f1[i] > 0:
            if j >= i and f2[j] != 0:
                return False
            if f1[i] >= f2[j]:
                f1[i] -= f2[j]
                f2[j] = 0
                j += 1
            else:
                f2[j] -= f1[i]
                f1[i] = 0
    return sum(f2) == 0


m, n = map(int, input().split())
arr = list(map(int, input().split()))

freq1 = [0] * (m + 1)
freq2 = [0] * (m + 1)
best = 0

for i in range(n // 2):
    freq1[arr[i]] += 1
    if i != 0:
        freq2[arr[i]] -= 1
        freq2[arr[i * 2]] += 1
    freq2[arr[i * 2 + 1]] += 1

    if is_greater(freq2.copy(), freq1.copy()):
        best = max(best, i + 1)

print(best)
