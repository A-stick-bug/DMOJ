n = int(input())
arr = [int(input()) for _ in range(n)]

arr.remove(max(arr))
print(sum(arr) // (n - 1))
