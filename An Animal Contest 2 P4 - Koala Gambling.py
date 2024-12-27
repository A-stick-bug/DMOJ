"""
https://dmoj.ca/problem/aac2p4
Put this in the middle
[a, b, a, b]
and put everything else 'around' it symmetrically
so for example [4,2,2,2, 1,5,1,5 ,2,2,2,4]
it doesn't matter what a and b are as long as they don't equal
"""

from collections import Counter


def solve():
    n = int(input())
    arr = sorted(map(int, input().split()))

    freq = Counter(arr)

    if any(v % 2 == 1 for v in freq.values()):  # trivial case: has odd frequencies
        print(" ".join(map(str, arr)))
    else:
        if len(freq) == 1:  # all equal and even frequency: tie
            print(-1)
            return

        f = freq.most_common()
        first = f[0][0]
        last = f[1][0]
        mid = [first, last, first, last]

        other = []
        for k in freq:
            if k == first:
                freq[k] -= 2
            if k == last:
                freq[k] -= 2
            other.extend([k] * (freq[k] // 2))

        final = (other + mid + other[::-1])
        print(" ".join(map(str, final)))


for _ in range(int(input())):
    solve()

"""
1
12
1 1 1 1 2 2 2 2 3 3 3 3
"""
