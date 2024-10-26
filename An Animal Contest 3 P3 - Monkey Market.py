"""
https://dmoj.ca/problem/aac3p3
Observation and intuition based question
Maximize the sum of (x_i * a_i / a_j)

Example: [1, 2, 3, 4]
possible arrangements with [BSBS], starting with $10:
1. [1, 3, 2, 5] -> $75
2. [1, 5, 2, 3] -> $75
3. [2, 3, 1, 5] -> $75
4. [2, 5, 1, 3] -> $75

Assumption: as long as we pair big with small, it works
"""

n = int(input())
arr = sorted(map(int, input().split()))

hf = n // 2
small = arr[:hf]  # smaller half
big = arr[hf:]  # bigger half, may have 1 extra element
big.append(big.pop(0))  # if there's an extra element, move the smallest to the back so we don't use it

order = []
operations = "BS" * hf  # alternate, buy small, sell big
for i in range(hf):
    order.append(small[i])
    order.append(big[i])

if len(big) > len(small):  # extra element due to odd parity, ignore it
    order.append(big[-1])
    operations += "E"

print(" ".join(map(str, order)))
print(operations)
