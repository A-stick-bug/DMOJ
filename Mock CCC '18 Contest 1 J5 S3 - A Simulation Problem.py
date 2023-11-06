# https://dmoj.ca/problem/nccc1j5s3
# this problem can be reduced to search for first valid element (using binary search)

# the function to simulate
def function(N):
    threshold = N * (N - 1) / 2  # sum of numbers from 1 to N-1
    K = 1
    count = 0  # cumulated sum
    while K < N:
        L = K + 1
        print(K)
        # adds N-K to count until half of threshold is passed
        # K starts at 1, so its sum(N-1, N-2 ...)
        # basically just binary search for when half the threshold is passed
        while L <= N:
            count += 1
            L += 1
            if 2 * count >= threshold:
                return
        K += 1


def range_sum(start, end):
    # sum of elements of [start, end], similar to querying a prefix sum
    return end * (end + 1) // 2 - start * (start - 1) // 2


n = int(input())
threshold = n * (n - 1) // 2

low = 0
high = n
while low <= high:
    mid = (low + high) // 2
    if range_sum(n - mid, n - 1) >= threshold / 2:  # first valid element template
        high = mid - 1
    else:
        low = mid + 1

print(low)
