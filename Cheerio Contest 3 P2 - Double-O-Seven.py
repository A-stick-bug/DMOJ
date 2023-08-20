# play greedily:
# opponent blocks: reload
# opponent shoots: block
# opponent reloads: shoot or reload

n = int(input())
moves = input()

score = 0
ammo = 0
opponent_ammo = 0
for move in moves:
    if move == "R":
        opponent_ammo += 1
        if ammo > 0:  # shoot
            ammo -= 1
            score += 1
        else:  # reload
            ammo += 1

    elif move == "F":
        if opponent_ammo == 0:  # does nothing
            if ammo > 0:  # shoot
                ammo -= 1
                score += 1
            else:  # reload
                ammo += 1
        else:  # just block and nothing happens
            opponent_ammo -= 1

    elif move == "B":
        ammo += 1  # reload

print(score)
