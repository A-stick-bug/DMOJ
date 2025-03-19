# https://dmoj.ca/problem/bfs19p3
# Greedy algorithm + sliding window
# Always remove as many characters as possible
# To minimize the sum of squares, remove from the largest element
#
# Brute force the substring part and optimize the removing character part
#
# TC: O(26n)

import sys

inf = 1 << 60
s = list(map(lambda x: ord(x) - ord("a"), input()))
L, K = map(int, input().split())
N = len(s)

f_arr = [0] * 26
for i in s:
    f_arr[i] += 1

if L + K >= N:
    print(0)
    sys.exit()


def get_best(arr: list[int]) -> int:
    """Return the minimum sum of squares of `arr` after subtracting a total of K"""
    arr.sort(reverse=True)
    arr.append(0)  # padding
    cur = K
    for i in range(26):
        if arr[i] > arr[i + 1]:
            # 'flatten' the highest elements simultaneously to the next highest
            diff = (i + 1) * (arr[i] - arr[i + 1])
            if diff <= cur:
                cur -= diff
            else:
                for j in range(i):  # apply flattening
                    arr[j] = arr[i]
                # spread removals evenly
                rem_all = cur // (i + 1)
                cur -= rem_all * (i + 1)
                for j in range(i + 1):
                    arr[j] -= rem_all
                # extra removals
                for j in range(cur):
                    arr[j] -= 1
                return sum(i ** 2 for i in arr)
    return 0


freq = [0] * 26
ans = inf

if L == 0:
    ans = get_best(f_arr)
else:
    for i in range(N):
        freq[s[i]] += 1
        if i + 1 >= L:  # window is large enough
            ans = min(ans, get_best([i - j for i, j in zip(f_arr, freq)]))
            freq[s[i - L + 1]] -= 1
print(ans)
