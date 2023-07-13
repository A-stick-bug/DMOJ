#finished 5/5

def bubble_sort(arr):
    n = len(arr)

    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


arr = []
times = int(input())
time = 0
while time < times:
    time += 1
    num = int(input())
    arr.append(num)

bubble_sort(arr)

for arrs in arr:
    print(arrs)
