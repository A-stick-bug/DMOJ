# brute force all combinations and add it if the sum is less than t
# then, sort each combination and the whole thing

n, t = map(int, input().split())

moves = []
costs = []
for _ in range(n):
    move, cost = input().split()
    moves.append(move)
    costs.append(int(cost))

# get all 3-card combinations
all_comb = []
for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            if costs[i] + costs[j] + costs[k] <= t:
                all_comb.append([moves[i], moves[j], moves[k]])

all_comb = list(map(sorted, all_comb))  # sort each combination
all_comb = [" ".join(comb) for comb in all_comb]  # turn into strings
all_comb.sort()  # sort the whole thing

for c in all_comb:
    print(c)
