# MLE, check C++ code

N, M = map(int, input().split())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))
arr1.sort()
arr2.sort()


def works(x):
    """check if a min difference of x works"""
    i = j = 0
    cnt = 0
    while i < N and j < M:
        if abs(arr1[i] - arr2[j]) > x:
            if arr1[i] > arr2[j]:
                j += 1
            else:
                i += 1
        else:
            i += 1
            j += 1
            cnt += 1

    return cnt == min(N, M)


low = 0
high = min(N, M)
while low <= high:
    mid = (low + high) // 2
    if works(mid):
        high = mid - 1
    else:
        low = mid + 1

print(low)
