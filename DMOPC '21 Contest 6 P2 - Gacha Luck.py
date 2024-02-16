"""
https://dmoj.ca/problem/dmopc21c6p2

Observation: it is never optimal to include ones, here's an example:
[0, 0, 1, 0]: if we take the 2 zeros, your score is 2, if we take everything, our score is ceil(3/2) = 2

After that, it's just grouping, sorting, and taking the K biggest groups.
"""

N, K = map(int, input().split())
arr = list(map(int, list(input())))

groups = [0]
for i in range(N):
    if arr[i] == 0:
        groups[-1] += 1
    else:
        groups.append(0)

groups.sort(reverse=True)
print(sum(groups[:K]))
