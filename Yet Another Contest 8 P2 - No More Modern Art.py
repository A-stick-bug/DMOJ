# remember that xor is associative and commutative
# then you notice everything except the last pair cancels out

n, x = map(int, input().split())
arr = list(map(int, input().split()))

seen = set()
for i in range(n):
    if arr[i] ^ x in seen:
        print("YES")
        __import__("sys").exit()
    seen.add(arr[i])
print("NO")
