"""
https://dmoj.ca/problem/aac5p2
Interactive problem
"""

n = int(input())
answers = []

for i in range(1, n):
    print("?", 1, i + 1)
    answers.append(int(input()))

first = min(answers)
if max(answers) == n:
    first = 1
res = [first]
for i in range(1, n):
    res.append(answers[i - 1] // first)
print("!", *res)

# 5
# ? 1 2
# 12
# ? 1 3
# 8
# ? 1 4
# 4
# ? 1 5
# 20
