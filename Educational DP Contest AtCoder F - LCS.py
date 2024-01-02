# https://dmoj.ca/problem/dpf
# LCS but we need to keep track of the next letter to build the LCS after filling in the DP table

s = input()
t = input()
n, m = len(s), len(t)

dp = [[0] * (m + 1) for _ in range(n + 1)]
after = [[-1] * (m + 1) for _ in range(n + 1)]

table = {1: (1, 1), 2: (1, 0), 3: (0, 1)}

for i in reversed(range(n)):
    for j in reversed(range(m)):
        if s[i] == t[j]:
            dp[i][j] = 1 + dp[i + 1][j + 1]
            after[i][j] = 1  # 1 means (i+1, j+1)

        else:
            if dp[i + 1][j] > dp[i][j + 1]:
                dp[i][j] = dp[i + 1][j]
                after[i][j] = 2  # 2 means (i+1, j)
            else:
                dp[i][j] = dp[i][j + 1]
                after[i][j] = 3  # 3 means

i, j = 0, 0
res = []
while after[i][j] != -1:
    cmd = after[i][j]
    if cmd == 1:
        res.append(s[i])
    d_i, d_j = table[cmd]
    i += d_i
    j += d_j

print("".join(res))
