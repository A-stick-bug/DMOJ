"""
https://dmoj.ca/problem/tc18summerb
Observations:
- we treat number[i] as the i-th bit of that numer
- corner case: if OR[i] == 0 and AND[i] == 1, it is impossible (MY CODE BREAKS HERE BUT WEAK DATA)
- if OR[i] == AND[i], A[i] and B[i] are fixed
- if OR[i] == 1 and AND[i] == 0, we can have A[i]=0, B[i]=1 or vice versa (2 choices)
- We just need to count the number of 1s in XOR (which is how many times A[i] != B[i])
- Note: also make sure OR, AND, and XOR are consistent or else there are no answers
"""

OR, AND, XOR = map(int, input().split())
if OR ^ AND != XOR:
    print(0)
else:
    print(1 << (bin(XOR).count("1")))
