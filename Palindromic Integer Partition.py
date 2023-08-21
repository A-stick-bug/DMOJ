# # Math solution, 1-liner
# print(2**(int(input())//2))

# O(n) solution using combinatorics

n = int(input())
total = 0
partition = lambda x: 2 ** (x - 1)

if n % 2 == 1:  # for odd, the middle is 1 number, n-mid must be even so that both sides can be made equal
    for i in range(1, n - 1, 2):
        total += partition((n - i) // 2)

else:  # for even numbers, the middle can be 1 number or be split into 2 numbers
    for i in range(2, n - 1, 2):
        total += partition((n - i) // 2) * 2  # therefore, we multiply the partitions by 2

    total += 1  # special case of (n/2, n/2), occurs on all even numbers

print(total + 1)  # +1 because n itself counts
