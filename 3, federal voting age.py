
repeat_times = int(input())
current_time = 0
output = []
# 1989/2/27
while current_time < repeat_times:

    current_time += 1
    birthdate = str(input())
    birthdate = birthdate.split(" ")

    if int(birthdate[0]) < 1989:
        output.append("Yes")
    elif int(birthdate[0]) == 1989:
        if int(birthdate[1]) < 2:
            output.append("Yes")
        elif int(birthdate[1]) == 2:
            if int(birthdate[2]) <= 27:
                output.append("Yes")
            else:
                output.append("No")
        else:
            output.append("No")
    else:
        output.append("No")

for i in output:
    print(i)
