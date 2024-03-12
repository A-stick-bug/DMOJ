"""
https://dmoj.ca/problem/egoi21p2

Using Fenwick Tree as a stack

For most of these questions where you need to pair things up, consider a stack
Looking at the commented code below, we can see that a stack does indeed work, it is just inefficient

How can we remove an element from a stack in < O(n)? Well we don't really need to.
Notice that the only operation on the stack is stack.index(i), we can simply use a Fenwick Tree to get this value
in log(n), note that the fenwick tree needs point query and range update
"""


class FenwickTree2:  # range update, point query, 1-indexed
    def __init__(self, n):
        self.bit = [0] * (n + 1)

    def add(self, i, val):
        while i < len(self.bit):
            self.bit[i] += val
            i += i & -i

    def range_add(self, l, r, val):
        self.add(l, val)
        self.add(r + 1, -val)

    def query(self, i):
        ret = 0
        while i > 0:
            ret += self.bit[i]
            i -= i & -i
        return ret


n = int(input())
arr = list(map(int, input().split()))

moves = 0

stack = FenwickTree2(2 * n)  # stack.query(pos[i]) == stack.index(i)
pos = [-1] * (n + 1)  # the position of person i in the Fenwick Tree
length = 0
cur_idx = 1

for i in arr:
    if pos[i] != -1:  # in stack, therefore seen before
        moves += length - stack.query(pos[i]) - 1  # takes this many moves to pair up this person

        # 'removed' the current element, minus 1 from the index of everything after it as they are shifted left
        stack.range_add(pos[i], cur_idx - 1, -1)
        length -= 1

    else:  # add current element to stack (first available position at the end of the BIT)
        pos[i] = cur_idx
        stack.range_add(cur_idx, cur_idx, length)
        cur_idx += 1
        length += 1

print(moves + n)  # add the steps to remove each pair

# # attempt 1: no optimization: O(N^2)
# n = int(input())
# arr = list(map(int, input().split()))
#
# moves = 0
# stack = []  # removing elements from middle of a stack be like
# for i in arr:
#     if i in stack:
#         moves += len(stack) - stack.index(i) - 1
#         stack.remove(i)
#     else:
#         stack.append(i)
#
# print(moves + n)
