# https://dmoj.ca/problem/dmopc20c6p1
# 2 pointers, O(n)
# move second pointer forwards so that the halfway point is between j and j+1, just check both and take the best answer

n = int(input())
arr = list(map(int, input().split())) * 2

total = sum(arr) // 2
hf = total // 2
res = [0] * n

j = -1
cur = 0
for i in range(n):
    while arr[j + 1] + cur < hf:  # move right pointer so that the current range is just less than half
        cur += arr[j + 1]
        j += 1

    res[i] = min(abs(total - cur - cur), abs(total - 2 * (cur + arr[j + 1])))  # check both j and j+1
    cur -= arr[i]  # move left pointer

print(*res)
