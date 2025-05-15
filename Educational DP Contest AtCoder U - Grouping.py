# TLE, CHECK C++ CODE FOR EXPLANATION
# https://dmoj.ca/problem/dpu

def solve():
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]

    value = [0] * (1 << n)
    for mask in range(1 << n):
        res = 0
        for i in range(n):
            for j in range(i + 1, n):
                if mask & (1 << i) and mask & (1 << j):
                    res += arr[i][j]
        value[mask] = res

    n_exp = 1 << n
    inf = 1 << 60
    dp = [-inf] * n_exp
    dp[-1] = 0  # base case: all taken

    for taken in reversed(range(n_exp - 1)):
        available = [i for i in range(n) if not taken & (1 << i)]
        m = len(available)
        best = 0
        for submask in range(1, 1 << m):  # find a method without the N factor to loop submasks
            bits = []
            for i in range(m):
                if submask & (1 << i):
                    bits.append(available[i])
            nxt_mask = 0
            for i in bits:
                nxt_mask |= 1 << i
            new_taken = taken | nxt_mask
            best = max(best, value[nxt_mask] + dp[new_taken])
        dp[taken] = best

    print(dp[0])


solve()
