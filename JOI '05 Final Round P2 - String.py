def apply_operation(s):
    groups = []
    cur = 1
    for i in range(1, len(s)):
        if s[i] != s[i - 1]:
            groups.append((s[i - 1], cur))
            cur = 1
        else:
            cur += 1
    groups.append((s[-1], cur))
    return "".join(str(group[1]) + group[0] for group in groups)


n = int(input())
s = input()

for _ in range(n):
    s = apply_operation(s)
print(s)
