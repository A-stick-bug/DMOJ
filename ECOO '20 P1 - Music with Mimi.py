# https://dmoj.ca/problem/ecoo20p1
# Painful implementation question

notes = "C C# D D# E F F# G G# A A# B".split()


def works(arr):
    arr = list(map(lambda x: notes.index(x), arr))
    for i in range(1, 4):
        if arr[i] < arr[i - 1]:
            arr[i] += len(notes)
    diff = [arr[i + 1] - arr[i] for i in range(3)]
    return diff[0] == 4 and diff[1] == diff[2] == 3


for _ in range(int(input())):
    arr = input().split()
    cnt = 0
    while cnt < 4 and not works(arr):
        cnt += 1
        arr.insert(0, arr.pop())

    print(["root", "first", "second", "third", "invalid"][cnt])
