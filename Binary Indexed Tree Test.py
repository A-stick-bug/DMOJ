def update(x, a, v):
    while x < len(a):
        a[x] += v
        x += (x & -x)


def query(x, a):
    total = 0
    while x > 0:
        total += a[x]
        x -= (x & -x)
    return total


n, queries = map(int, input().split())
arr = list(map(int, input().split()))

bit = [0] * (len(arr) + 1)
freq = [0] * 100001

# create BIT
for i in range(1, n + 1):
    var = arr[i - 1]
    update(i, bit, var)
    update(var, freq, 1)

for _ in range(queries):
    line = input().split()
    q = line[0]
    if q == 'C':
        a, b = int(line[1]), int(line[2])
        v = arr[a - 1]
        update(a, bit, b - v)
        update(v, freq, -1)
        update(b, freq, 1)
        arr[a - 1] = b

    elif q == 'S':
        a, b = int(line[1]), int(line[2])
        print(query(b, bit) - query(a - 1, bit))

    else:
        a = int(line[1])
        print(query(a, freq))
