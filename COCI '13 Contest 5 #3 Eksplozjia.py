# MLE, 5/15
# quite similar to the valid parenthesis question (but the second string has length > 2)
# "The explosion will not contain two equal characters" makes it a lot easier

s = input()
bomb = input()
bomb_letters = set(bomb)
stack = []
deleted = set()  # contains indices of all deleted letters
full_bomb = True

if len(bomb) == 1:  # corner case
    s = s.replace(bomb, "")

for i, letter in enumerate(s):
    if letter not in bomb_letters:  # basically prevents any previous possible explosions
        stack.clear()
        full_bomb = False
        continue

    if letter == bomb[0]:  # start of a bomb
        stack.append((i, 0))  # index of character, index in bomb, letter
        full_bomb = True

    elif stack:
        bomb_index = stack[-1][1]
        if letter != bomb[bomb_index + 1]:  # doesn't match next letter in bomb
            stack.clear()
            full_bomb = False

        elif bomb_index == len(bomb) - 2 and full_bomb:  # matches next letter and is the last letter
            deleted.add(i)
            for _ in range(len(bomb) - 1):
                deleted.add(stack.pop()[0])

        else:  # matches same next letter in bomb, not the last one
            stack.append((i, bomb_index + 1))

if not s or len(deleted)==len(s):
    print("FRULA")
else:
    print(*[char if i not in deleted else "" for i, char in enumerate(s)], sep="")
