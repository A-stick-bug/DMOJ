# just apply PSA

from itertools import accumulate
import sys

input = sys.stdin.readline
N, M, K = map(int, input().split())

for _ in range(N):
    row = list(input())
    ans = row.copy()
    A = [i == "A" for i in row]
    B = [i == "B" for i in row]

    psa_a = [0] + list(accumulate(A))
    psa_b = [0] + list(accumulate(B))
    query = lambda psa, l, r: psa[r + 1] - psa[l]

    for i in range(M):
        if row[i] == ".":
            continue
        elif row[i] == "A":  # score right
            if i == M - 1 or query(psa_b, i + 1, min(M - 1, i + K)) == 0:
                ans[i] = "Y"
            else:
                ans[i] = "N"

        elif row[i] == "B":  # score left
            if i == 0 or query(psa_a, max(0, i - K), i - 1) == 0:
                ans[i] = "Y"
            else:
                ans[i] = "N"

    print("".join(ans))
