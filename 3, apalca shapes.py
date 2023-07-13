#3/3 finished

num = input()
new_num = num.split()

if int(new_num[0]) ** 2 > (int(new_num[1]) ** 2) * 3.14:
    print("SQUARE")
else:
    print("CIRCLE")
