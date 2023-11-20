n = int(input())
s = input()
s = [i for i in range(2 * n) if s[i] == "I"]  # indices of I
print(sum(abs(i * 2 - s[i]) for i in range(n)))
