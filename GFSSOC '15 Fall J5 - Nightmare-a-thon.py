import sys

input = sys.stdin.readline

n, q = map(int, input().split())
ratings = list(map(int, input().split()))

freq_left, max_left = [1], [ratings[0]]
for i in range(1, n):
    if ratings[i] > max_left[-1]:
        max_left.append(ratings[i])
        freq_left.append(1)
    else:
        max_left.append(max_left[-1])
        if ratings[i] == max_left[-1]:
            freq_left.append(freq_left[-1] + 1)
        else:
            freq_left.append(freq_left[-1])

freq_right, max_right = [0] * n, [0] * n
freq_right[-1] = 1
max_right[-1] = ratings[-1]
for i in reversed(range(n - 1)):
    if ratings[i] > max_right[i + 1]:
        max_right[i] = ratings[i]
        freq_right[i] = 1
    else:
        max_right[i] = max_right[i + 1]
        if ratings[i] == max_right[i + 1]:
            freq_right[i] = freq_right[i + 1] + 1
        else:
            freq_right[i] = freq_right[i + 1]

# print(max_left, freq_left, max_right, freq_right, sep="\n")

for _ in range(q):
    start, end = map(int, input().split())
    highest_left = 0 if start == 1 else max_left[start-2]
    highest_right = 0 if end == n else max_right[end]
    highest = max(highest_left, highest_right)

    if highest_left > highest_right:
        freq_max = freq_left[start-2]
    elif highest_right > highest_left:
        freq_max = freq_right[end]
    else:
        freq_max = freq_left[start-2] + freq_right[end]

    print(highest, freq_max)
