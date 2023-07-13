# CCC '07 J1 - Who is in the Middle?
# Canadian Computing Competition: 2007 Stage 1, Junior #1

#finished 3/3

first = int(input())
second = int(input())
third = int(input())

if first > second and first < third:
    print(first)
if first < second and first > third:
    print(first)
if second > first and second < third:
    print(second)
if second < first and second > third:
    print(second)
if third > first and third < second:
    print(third)
if third < first and third > second:
    print(third)
