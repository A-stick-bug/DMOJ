"""
https://dmoj.ca/problem/dmopc21c9p1
Fun math question (with basic algebra)

- By setting the first element of the array to X, the entire array is fixed
- We just check how many valid values there are for X (it is guaranteed to be a contiguous interval)
- Using simple algebra we can keep track of the valid interval

i=0     i=1      i=2           i=3
------------------------------------------
    5        4            3
X      5-x      4-(5-x)       3-(x-1)
                = x-1         = 4-x

We do interval calculations for each index
eg. i=1: 5-x>0 -> x<=4  [1,4]
    i=2: x-1>0 -> x>=2  [2,4]
    i=3: 4-x>0 -> x<=3  [2,3]
Answer: (3-2+1) = 2
"""

n = int(input())
arr = list(map(int, input().split()))

low = 1  # inclusive range
high = 10**9

const = 0
for i in range(n - 1):
    const = -(const - arr[i])  # update the constant in (+/-)x + const
    if i % 2 == 0:
        high = min(high, const - 1)  # -x+const > 0
    else:
        low = max(low, -const + 1)  # x-const > 0

print(max(0, high - low + 1))  # note: we print invalid intervals as 0
