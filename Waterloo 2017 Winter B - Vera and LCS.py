"""
https://dmoj.ca/problem/waterloo2017wb
note: it may be helpful to write the LCS code and randomly generate data to see where your code breaks

Strategy:
- drawing uncrossing lines between 2 strings is the perfect way to visualize this problem
- get the least occurring character, keep this character the same in all its positions
   - observe that |LCS| is at least the frequency of this character as we can just match all of its occurrences
- as for the other characters, we copy it if we need to increase |LCS| to match K
- otherwise, just set it to the least occurring character as it won't increase LCS (can't match it to anything in s)
"""

from collections import Counter
import sys

n, k = map(int, input().split())
s = input()
freq = Counter(s)

least = "a"  # get least occurring character
for char in "qwertyuiopasdfghjklzxcvbnm":
    if freq[char] < freq[least]:
        least = char

if freq[least] > k or k > n:  # too many or too little common characters
    print("WRONGANSWER")
    sys.exit()

res = ["?"] * n
k -= freq[least]
for i in range(n):
    if least == s[i]:  # keep letter same
        res[i] = s[i]
    elif k > 0:  # not enough matched letters, copy letter over
        res[i] = s[i]
        k -= 1
    else:  # enough matched letters, setting as the least common letter guarantees it won't increase the LCS
        res[i] = least

print("".join(res))

# # LCS code for reference
# def lcs(nums1, nums2) -> int:
#     n, m = len(nums1), len(nums2)
#     dp = [[0] * (m + 1) for _ in range(n + 1)]
#     for i in reversed(range(n)):
#         for j in reversed(range(m)):
#             if nums1[i] == nums2[j]:
#                 dp[i][j] = 1 + dp[i + 1][j + 1]
#             else:
#                 dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])
#
#     return dp[0][0]
