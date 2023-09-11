# standard fenwick tree operations, nothing special here
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
    # we need a BIT for the frequency array to answer the
    # how many elements are less than or equal to v in the array queries
    update(var, freq, 1)

for _ in range(queries):
    line = input().split()
    q = line[0]
    if q == 'C':
        a, b = int(line[1]), int(line[2])
        v = arr[a - 1]  # element to be changed
        update(a, bit, b - v)  # adding (new_element - previous_element) will turn the previous element to b
        update(v, freq, -1)  # -1 for the element that got changed
        update(b, freq, 1)  # +1 for the new element
        arr[a - 1] = b  # update out original array

    elif q == 'S':
        a, b = int(line[1]), int(line[2])
        print(query(b, bit) - query(a - 1, bit))  # query is same as prefix sum

    else:
        a = int(line[1])
        print(query(a, freq))  # querying the frequency array will give us the number of elements less than v
