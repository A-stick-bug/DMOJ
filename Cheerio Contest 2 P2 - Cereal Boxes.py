# https://dmoj.ca/problem/cheerio2p2
# binary search with arithmetic sequence formula

def works(val):  # check if we can pay for val with Q
    d, r = divmod(val, M)

    total = 0
    total += M * (d * (C + C + (d - 1) * I)) // 2
    total += r * (C + d * I)

    return total <= Q


M, C, I, Q = map(int, input().split())

low = 0
high = 10 ** 18
while low <= high:
    mid = (low + high) // 2
    if works(mid):
        low = mid + 1
    else:
        high = mid - 1
print(low - 1)
