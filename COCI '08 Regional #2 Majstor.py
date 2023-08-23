def points(mine, opponents):
    if mine == opponents:
        return 1
    elif mine == "R" and opponents == "S":
        return 2
    elif mine == "S" and opponents == "P":
        return 2
    elif mine == "P" and opponents == "R":
        return 2
    return 0


R = int(input())
moves = input()

n_friends = int(input())
friends = [list(input()) for _ in range(n_friends)]
turns = list(zip(*friends))

total = 0
total_best = 0

for i in range(R):
    move = moves[i]
    opp = turns[i]
    score = sum([points(move, opp[j]) for j in range(n_friends)])
    optimal = max(sum([points("R", opp[j]) for j in range(n_friends)]),  # try all possible moves to get optimal
                  sum([points("P", opp[j]) for j in range(n_friends)]),
                  sum([points("S", opp[j]) for j in range(n_friends)]))

    total += score
    total_best += optimal

print(total)
print(total_best)

