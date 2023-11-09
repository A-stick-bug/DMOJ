# when reversing, we can only combine at both ends
# first deal with the start and ends, after that, just find the number of 'groups' of the same characters

n = int(input())
s = input()

total = 0

# first get the start and end, all same characters can be reduced to 1
if s[0] == s[-1]:
    total += 1
    s = s.strip(s[0])

    prev = "."  # placeholder
    for char in s:
        if char != prev:
            prev = char
            total += 1
    print(total)

else:
    print(n)
