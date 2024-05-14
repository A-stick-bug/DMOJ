MOD = 10 ** 9 + 7
n = int(input())

if n < 3:
    print([-1, 1, 2][n])
else:
    dp = [0] * (n + 1)
    dp[0] = 0
    dp[1] = 1
    dp[2] = 1
    for i in range(3, n + 1):
        dp[i] = (dp[i - 1] + dp[i - 3]) % MOD

    print(sum(dp) % MOD)

"""
for i in [1-n]:
    add how many good arrays with length i there are with max number being n

# of good arrays of length i =
# of ways to choose numbers from [i, n] such that no 2 are consecutive

[1,2,4,7,12,16]

[1][2][3][4][5][6]
[1,3][2,4][3,5][4,6][1,4][2,5][3,6]
[1,3,5][1,3,6][1,4,6]

n = 4
1 [1 number in [1,4]] -> [1],[2],[3],[4]
2 [2 numbers in [2,4]] -> [2 numbers in [1,3]]
3 0
4 0

"""
