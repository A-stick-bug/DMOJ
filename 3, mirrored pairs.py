print("Ready")
mirrored = ["qp", "pq", "bd", "db"]

while True:
    pair = input()
    if pair in mirrored:
        print("Mirrored pair")
    elif pair == "  ":
        break
    else:
        print("Ordinary pair")

#finished, 3/3
