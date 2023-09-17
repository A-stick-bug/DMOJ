"""
https://dmoj.ca/problem/dmopc14c2p6

Key realization: the queries do not need to be done in order

Using offline query and Fenwick Tree
- sort queries and trees in descending order by mass (save the location/index as well)
- for each query, we first add the trees that have a higher mass than q (using .update)
- after that, just get the answer with .update

"""


class FenwickTree:
    def __init__(self, size: int):
        self.bit = [0] * (size + 1)

    def update(self, i: int, diff: int) -> None:
        while i < len(self.bit):
            self.bit[i] += diff
            i += i & (-i)

    def query(self, i: int):
        total = 0
        while i > 0:
            total += self.bit[i]
            i -= i & (-i)
        return total


N = int(input())
arr = [(int(val), i) for i, val in enumerate(input().split())]  # (mass, index) sort by mass
arr.sort(reverse=True)

Q = int(input())
queries = [[i] + list(map(int, input().split())) for i in range(Q)]  # (index, l, r, min_mass) sort by min_mass
queries.sort(key=lambda x: x[3], reverse=True)

# start with an empty BIT
bit = FenwickTree(N)
answers = [-1] * Q
arr_index = 0

for i, left, right, lowest in queries:
    left += 1  # BIT uses 1-indexing
    right += 1

    # add the trees with a >= mass than lowest, the trees that are already added are guaranteed to have a higher mass
    # because the queries are sorted in descending order
    while arr_index < N and arr[arr_index][0] >= lowest:
        val, index = arr[arr_index][0], arr[arr_index][1]
        bit.update(index + 1, val)  # +1 for 1-indexing
        arr_index += 1

    # query range, current BIT only contains trees with mass >= lowest, this gives us the answer to the i-th query
    answers[i] = bit.query(right) - bit.query(left - 1)

# print queries in their original order in input
for ans in answers:
    print(ans)
