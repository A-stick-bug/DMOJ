# https://dmoj.ca/problem/dmopc21c5p3
# reference: https://oeis.org/A072545
# I cannot justify any of my logic, it's purely finding patterns on OEIS and applying them
# ALl observations are made with the winner() code and brute force
#
# First observe that [1,2,3,...,n] usually works
# Find on OEIS the numbers that don't work
# Notice that very few odd numbers don't work, but we can brute force those by iterating permutations
# Notice that to make the even numbers work, we can swap the last 2 numbers
#
# TC: O(n) per test case, ignore special cases which we can hardcode

from itertools import permutations

MN = 10 ** 5 + 1
is_prime = [True] * MN
is_prime[0] = is_prime[1] = False
for i in range(2, int(MN ** 0.5) + 1):
    if is_prime[i]:
        for j in range(i * i, MN, i):
            is_prime[j] = False

# this is our list of 'special cases' where [1,2,3,...,n] doesn't work
A072545 = [1, 2, 10, 11, 26, 35, 36, 50, 56, 86, 92, 101, 116, 122, 126, 134, 146, 156, 170, 176, 188, 196, 206, 218,
           236, 248, 254, 260, 266, 290, 296, 302, 310, 311, 320, 326, 336, 344, 356, 362, 376, 386, 392, 396, 404, 416,
           426, 446, 452, 470, 476, 482, 486, 494]
while A072545[-1] < 10 ** 5:
    found = False
    for k in range(A072545[-1] + 4, MN, 2):
        if all(not is_prime[k - diff] for diff in [1, 11, 35, 101, 311]):
            found = True
            A072545.append(k)
            break
    if not found:
        break
# print(A072545)
A072545 = set(A072545)


def winner(arr):  # check if 1st player wins starting with arr
    n = len(arr)
    start = arr.index(n)
    dp = [-1] * n

    def dp_solve(cur):
        if dp[cur] != -1:
            return dp[cur]
        w = False
        for i in range(n):
            if is_prime[abs(i - cur)] and arr[cur] > arr[i]:
                w = w or not dp_solve(i)
        dp[cur] = w
        return w

    return dp_solve(start)


lose = [11, 12, 35, 36, 101, 102, 311, 312]
t = int(input())
for _ in range(t):
    n = int(input())

    if n == 1 or n == 2:
        print(-1)
    elif n in lose:  # special cases
        arr = list(range(1, n + 1))
        for perm in permutations(arr):
            if winner(perm):
                print(" ".join(map(str, perm)))
                break
    else:
        a = list(range(1, n + 1))
        if n % 2 == 1 or (n % 2 == 0 and n not in A072545):
            print(" ".join(map(str, a)))
        else:
            a[-1], a[-2] = a[-2], a[-1]
            print(" ".join(map(str, a)))

# # find cases where [1,2,3,...,n] doesn't work
# # this matches with A072545
# losing = []
# for i in range(1, 1000):
#     a = list(range(1, i + 1))
#     plain = winner(a)
#
#     # if i % 2 == 0:
#     #     a[-1], a[-2] = a[-2], a[-1]
#     #
#     # res = winner(a)
#
#     if not plain:
#         losing.append(i)
#         print(i, plain, a)
# print(losing)
