# https://dmoj.ca/problem/halloween14p2
# Using a stack as a persistent data structure
# Binary search + PSA for optimization (I see these 2 topics together so often for some reason)
#
# - when we remove a cat, simply pop the last element in the stack to revert the change
# - when adding a cat, check if it can produce a better answer if we select a suffix with width <= W
#   - use binary search + psa to find the suffix

import sys

input = sys.stdin.readline
N, W = map(int, input().split())

psa_w = [0]
psa_c = [0]
query = lambda l, r, psa: psa[r + 1] - psa[l]

history = []
for _ in range(N):
    q = input().split()
    if q[0] == "D":  # revert back to previous best
        history.pop()
        psa_c.pop()
        psa_w.pop()

    else:
        width, c = map(int, q[1:])
        psa_w.append(psa_w[-1] + width)  # add new cat
        psa_c.append(psa_c[-1] + c)

        low = 0
        high = len(psa_c) - 2  # find the maximum gain we can get from the suffix
        while low <= high:
            mid = (low + high) // 2
            if query(mid, len(psa_w) - 2, psa_w) <= W:
                high = mid - 1
            else:
                low = mid + 1

        suffix = query(low, len(psa_c) - 2, psa_c)
        if not history:
            history.append(suffix)
        else:
            history.append(max(history[-1], suffix))  # the suffix sum may be greater than previous best

        print(history[-1])

