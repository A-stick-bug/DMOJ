n, m = map(int, input().split())

inv = 244002641
mod = 2 ** 32
arr = [int(input()) for _ in range(n)]
arr = list(map(lambda x: x * inv % mod, arr))
arr.sort(reverse=True)

print(sum(arr[:m]))
