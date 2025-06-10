# https://dmoj.ca/problem/mathp2
# Each element appears in exactly 2^{n-1} subsequences

MOD = 10 ** 9 + 7
n = int(input())
arr = list(map(int, input().split()))

print(sum(arr) * pow(2, n - 1, MOD) % MOD)
