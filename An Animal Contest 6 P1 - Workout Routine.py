# fill 1 to N-1, use last number to make the sum = 0 (mod K)

N, K = map(int, input().split())
arr = [i for i in range(1, N)]
s = sum(arr)

res = K - (s % K)
big = 10 ** 8

arr.append(big // K * K + res)

print(" ".join(map(str, arr)))
