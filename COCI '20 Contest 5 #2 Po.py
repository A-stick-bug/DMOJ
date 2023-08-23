# https://dmoj.ca/problem/coci20c5p2

# O(n), using monotonic stack
# this solution works because "every two segments were either disjoint or one was completely contained in the other"
# watch out for the stupid corner case where i=0, and you don't need an extra enhancer (and don't put anything in stack)

n = int(input())
arr = list(map(int, input().split()))
stack = []

res = 0
for i in arr:
    while stack and i < stack[-1]:  # pop to keep stack increasing
        stack.pop()

    # if the current number is greater than the stack's maximum, we need an extra enhancement
    if i != 0 and (not stack or i > stack[-1]):
        res += 1
        stack.append(i)

print(res)
