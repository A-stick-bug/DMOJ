# https://dmoj.ca/problem/coci07c1p4
# state transitions make no sense
# interval DP

def pair_combo(a, b):
    if a == b == "?":  # () or [] or {}
        return 3
    elif ((a in match and match[a] == b) or
          (a == "?" and b in match.values()) or
          (a in match and b == "?")):  # regular pair
        return 1
    return 0  # no match


MOD = 100_000
n = int(input())
s = input()

match = {"(": ")", "[": "]", "{": "}"}
dp = [[1] * n for _ in range(n)]  # dp[i][j]: number of possible valid sequences using [i,j]

for i in range(n - 1):  # base case: individual pairs
    dp[i][i + 1] = pair_combo(s[i], s[i + 1])

for length in range(3, n, 2):  # optimization: valid sequences are all even length
    for i in range(n - length):
        j = i + length
        dp[i][j] = 0
        for mid in range(i + 1, j, 2):  # combine 2 smaller intervals
            dp[i][j] += pair_combo(s[i], s[mid]) * dp[i + 1][mid - 1] * dp[mid + 1][j]
        dp[i][j] += pair_combo(s[i], s[j]) * dp[i + 1][j - 1]

# for i in dp:
#     print(i)
if dp[0][n - 1] >= MOD:
    print(f"{dp[0][n - 1] % MOD:05}")
else:
    print(dp[0][n - 1] % MOD)

"""
6
??{}()
"""
