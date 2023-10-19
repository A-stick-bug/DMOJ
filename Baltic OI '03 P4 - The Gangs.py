# https://dmoj.ca/problem/btoi03p4
# Using disjoint set data structure
# to maximize the number of groups, we only put people together in group if they must be in the same group

class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.rank = [1] * size

    def find(self, x):
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.root[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.root[rootX] = rootY
            else:
                self.root[rootY] = rootX
                self.rank[rootX] += 1


N = int(input())
M = int(input())

groups = UnionFind(N + 1)
enemies = [[] for _ in range(N + 1)]  # enemies[i] contains all the enemies of person i

for _ in range(M):
    fact = input().split()
    a, b = map(int, fact[1:])
    if fact[0] == "F":
        groups.union(a, b)  # if they are friends, we know they are in the same group right away
    else:
        enemies[a].append(b)  # if they are enemies, we process later
        enemies[b].append(a)

# group people based on their enemies
for i in range(1, N + 1):
    for enemy in enemies[i]:  # enemies of i
        for friend in enemies[enemy]:  # "An enemy of my enemy is my friend"
            groups.union(i, friend)

# count the total number of groups
all_groups = set()
for i in range(1, N + 1):
    all_groups.add(groups.find(i))

print(len(all_groups))
