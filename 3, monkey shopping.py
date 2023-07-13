message = input()

go_where = list(map(int,message.split()))

if (go_where[1] > go_where[0]) and (go_where[2] >= go_where[3]):
    print("Go to the grocery store")
elif (go_where[3] > go_where[2]) and (go_where[0] >= go_where[1]):
    print("Go to the pharmacy")
elif (go_where[0] >= go_where[1]) and (go_where[2] >= go_where[3]):
    print("Stay home")
elif (go_where[1] > go_where[0]) and (go_where[3] > go_where[2]):
    print("Go to the department store")
else:
    raise ValueError
