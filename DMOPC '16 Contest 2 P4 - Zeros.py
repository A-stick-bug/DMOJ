# https://dmoj.ca/problem/dmopc16c2p4
# Typical factorial question with binary search
# Note: trailing zeros is always bounded by the power of 5s
#       since 10 = 2*5 and 5 > 2 (5 appears less frequently)

def solve(z):
    """Find the maximum n such that n! has <=z trailing zeros."""
    low = 0
    high = 28
    ans = 0

    def count_p5(n):
        """count the powers of 5 in n!, standard division trick"""
        total = 0
        for p5 in range(1, 100):
            total += n // (5 ** p5)
        return total

    while low <= high:
        mid = (low + high) // 2
        if count_p5(mid) <= z:
            ans = mid
            low = mid + 1
        else:
            high = mid - 1
    return ans


a, b = map(int, input().split())

total = solve(b)
if a != 0:
    total -= solve(a - 1)

print(total)
