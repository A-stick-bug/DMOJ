# O(N*M), where n is the length of the string and m is the length of the bomb


s = input()
bomb = input()
nb = len(bomb)
lb = list(bomb)

stack = []
for char in s:
    stack.append(char)

    # trying to check for a match with bomb on every iteration is fine because the bomb is so small
    if len(stack) >= nb and stack[len(stack) - nb:] == lb:
        for i in range(nb):
            stack.pop()

print('FRULA') if not stack else print(''.join(stack))