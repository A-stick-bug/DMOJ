# https://dmoj.ca/problem/oly26practice3
# Track the index of `n` after each removal operation
#
# Time complexity analysis:
# - every iteration of the while loop, idx shrinks to idx*(k-1)/k
# - thus, we do log_{k/(k-1)}(n) iterations in total
# - I plotted this on Desmos, and it looks very close to k*log(n)
#
# TC: O(k * log(n))

n = int(input())
k = int(input())

idx = n - 1  # start at last index
move = 1
while True:
    if idx % k == k - 1:  # removed here
        print(move)
        break

    if idx < k - 1:  # n is not removed
        print(0)
        break

    # remove some elements to the left, reindex
    idx -= idx // k
    move += 1
