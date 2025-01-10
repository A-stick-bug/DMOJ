# https://dmoj.ca/problem/utso24p2
# greedy with prefix sums
# Try all options from one side and take the max from the other
# similar to https://dmoj.ca/problem/othscc1p4


from itertools import accumulate

n, k = map(int, input().split())
arr = list(map(int, input().split()))

pos = [0] + list(accumulate(sorted([i for i in arr if i > 0], reverse=True)))
neg = [0] + list(accumulate(sorted([-i for i in arr if i < 0], reverse=True)))

best = 0
for i in range(len(neg)):
    req = i * 2
    if req > k:
        break
    cur = neg[i] + pos[min(len(pos) - 1, k - req)]
    best = max(best, cur)

print(best)
