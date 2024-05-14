"""
https://dmoj.ca/problem/mathp7
Math trick and optimization
Consider using sieve on each possible factor
The # of integers with X as a factor is N//X
Therefore, we can just do (N//1 + N//2 + ... + N//N) for sum of # of factors

We can compute this in less than O(n) by grouping
For example, N = 6
6//1 + 6//2 + 6//3 + 6//4 + 6//5 + 6//6
 6      3      2    |------------------|
 skip 4,5           all of these equal 1

TC: not sure, O(sqrt(n))?
"""

n = int(input())
total = 0

i = n
while i > 0:
    res = n // i
    total += res * (i - n // (res + 1))  # multiply by the number of divisions with this value
    i = n // (res + 1)  # skip over elements in the group we just processed

print(total)

# # brute force code for reference
# n = int(input())
# total = 0
# for i in range(1, n+1):
#     total += n // i
# print(total)

"""
1: [1]           1   1
2: [1,2]         2   3
3: [1,3]         2   5
4: [1,2,4]       3   8
5: [1,5]         2   10
6: [1,2,3,6]     4   14
7: [1, 7]        2   16
8: [1,2,4,8]     4   20
9: [1,3,3]       2   23
"""
