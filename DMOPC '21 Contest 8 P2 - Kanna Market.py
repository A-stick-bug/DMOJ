# https://dmoj.ca/problem/dmopc21c8p2
# Ad hoc with lots of casework (and edge cases)


def fetch_constant(a1, a2):
    """returns what each column MUST sum to, if it exists"""
    val = 0
    for i, j in zip(a1, a2):
        if val == 0:
            if i != 0 and j != 0:
                val = i + j
        else:
            if i != 0 and j != 0 and i + j != val:
                return -1
    return val


def solve(a1, a2):
    c = fetch_constant(a1, a2)
    if c == -1:  # inconsistent values
        return 0

    elif c == 0:  # each row has at least 1 variable
        if sum(a1) + sum(a2) == 0:  # each row has 2 variables
            small = 2
            big = 2 * M
        else:
            small = max(i for i in a1 + a2 if i != 0) + 1  # each col must sum at least to this
            big = min(i for i in a1 + a2 if i != 0) + M  # each col can sum to at most this

        double = sum(i == j == 0 for i, j in zip(a1, a2))  # count the number of 0 0 pairs in columns
        ways = 0
        for i in range(small, big + 1):
            ways = (ways + pow(min(i - 1, M - (i - M) + 1), double, MOD)) % MOD
        return ways

    else:  # each column must sum to a fixed value
        ways = 1
        for i, j in zip(a1, a2):
            if i != 0 and j != 0:  # already fixed
                continue
            elif i == 0 and j == 0:  # 2 unknowns
                ways = (ways * min(c - 1, M - (c - M) + 1)) % MOD
            elif i == 0:
                if not (1 <= c - j <= M):  # not in range, too big or too small
                    return 0
            elif j == 0:
                if not (1 <= c - i <= M):  # not in range, too big or too small
                    return 0
        return ways


MOD = 10 ** 9 + 7
N, M = map(int, input().split())
a1 = list(map(int, input().split()))
a2 = list(map(int, input().split()))

even1 = [a1[i] for i in range(0, N, 2)]
odd1 = [a1[i] for i in range(1, N, 2)]
even2 = [a2[i] for i in range(0, N, 2)]
odd2 = [a2[i] for i in range(1, N, 2)]

ans = (solve(even1, even2) * solve(odd1, odd2)) % MOD
print(ans)

"""
Example Cases
4 3
0 0 0 0
0 0 0 0
361

3 2
0 1 2
1 1 2
0
"""
