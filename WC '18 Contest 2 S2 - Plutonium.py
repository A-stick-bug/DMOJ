import sys

n = int(input())
observed = list(map(int, input().split()))

if observed[0] > 1:  # this was stated by problem
    print(-1)
    sys.exit()

actual = observed.copy() + [0]  # prevent out of bounds error
for i in reversed(range(n)):
    if actual[i + 1] > 1:
        actual[i] = actual[i + 1] - 1

# for some reason without this, it breaks
# no idea why, but it works so lets just keep it there
observed[0] = 1

for i in range(n):
    if observed[i] != actual[i] and observed[i] != 0 and actual[i] != 0:
        print(-1)
        sys.exit()

zeros, ones = 0, 0
for i in range(1, n):
    if actual[i] == 0:
        zeros += 1
    elif actual[i] == 1:
        ones += 1

# print(observed)
# print(actual)
print(ones, zeros + ones)
