# https://dmoj.ca/problem/vmss7wc16c4p3
# classic LCS DP problem, fill table in reverse
# edit distance, but now each edit has a different cost
# for these questions, the trick is to ADD A COMMON LETTER at the end of both words

D, I, R = map(int, input().split())
s, t = input().split()  # min cost to s -> t
s += "."  # add common letter at the end of both words
t += "."
n, m = len(s), len(t)

dp = [[1 << 60] * (m + 1) for _ in range(n + 1)]  # dp[i][j] min cost at s[i] and t[j]
dp[n][m] = 0  # finished matching both words

for i in reversed(range(n)):
    for j in reversed(range(m)):
        if s[i] == t[j]:  # equal letters: no cost
            dp[i][j] = dp[i + 1][j + 1]
        else:  # not equal, take minimum cost
            dp[i][j] = min(D + dp[i + 1][j],  # delete character in s, match the next
                           I + dp[i][j + 1],  # insert, always insert correct character
                           R + dp[i + 1][j + 1])  # replace, match to correct character

print(dp[0][0])
