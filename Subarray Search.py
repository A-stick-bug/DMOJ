# https://dmoj.ca/problem/subsearch
# classic 2-pointer subarray count problem

from collections import defaultdict

N, F, S = map(int, input().split())
arr = list(map(int, input().split()))

j = 0
cur = 0
great = 0
for i in range(N):
    cur += arr[i]  # update running sum
    while cur > S:  # move j forwards until sum[i,j] <= S
        cur -= arr[j]
        j += 1
    great += i - j + 1  # all smaller subarrays ending at i are also 'great'

freq = defaultdict(int)
good = 0
j = 0
for i in range(N):
    freq[arr[i]] += 1
    while freq[arr[i]] > F:  # the only value that COULD be >F is the one we just added
        freq[arr[j]] -= 1
        j += 1
    good += i - j + 1

freq = defaultdict(int)  # repeat what we did with both conditions for great-good subarrays
cur = 0
both = 0
j = 0
for i in range(N):
    freq[arr[i]] += 1
    cur += arr[i]
    while freq[arr[i]] > F or cur > S:
        freq[arr[j]] -= 1
        cur -= arr[j]
        j += 1
    both += i - j + 1

print((good * great * both) % 1000000007)
