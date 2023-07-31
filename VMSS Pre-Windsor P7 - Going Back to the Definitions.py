from functools import cmp_to_key

# one liner solution
# print("".join(sorted([input() for _ in range(int(input()))], key=cmp_to_key(lambda x, y: int(y + x) - int(x + y)))))


def compare(x, y):
    return int(y + x) - int(x + y)


n = int(input())
nums = [input() for _ in range(n)]
nums.sort(key=cmp_to_key(compare))

print("".join(nums))
