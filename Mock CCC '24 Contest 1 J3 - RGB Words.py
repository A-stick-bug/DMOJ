n = int(input())
s = input() + "G"

cnt = []
cur = [0, 0]

for i,val in enumerate(s):
    if val == "R":
        cur[0] += 1
    elif val == "B":
        cur[1] += 1
    elif val == "G":
        cnt.append(cur.copy())
        cur = [0, 0]

total = 0
for i in range(len(cnt)-1):
    total += cnt[i][0] * cnt[i+1][1]
print(total)
