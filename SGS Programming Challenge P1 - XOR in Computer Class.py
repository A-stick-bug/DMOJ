# https://dmoj.ca/problem/sgspc1p1
# Each number contributes X*(n-i)*(i+1) to the subarray sum (left endpoint * right endpoint options)
# For each bit in our answer, check if flipping it will decrease the subarray sum

n = int(input())
arr = list(map(int, input().split()))

ans = 0
for bit in range(32):
    sum_reduction = 0
    for i in range(n):
        if arr[i] & (1 << bit):  # currently on, flipping it will reduce sum (for this many subarrays)
            sum_reduction += (n - i) * (i + 1)
        else:  # currently off, flipping it will increase sum
            sum_reduction -= (n - i) * (i + 1)

    if sum_reduction > 0:  # we should flip this bit iff it will reduce the subarray sum
        ans |= 1 << bit

print(ans)
