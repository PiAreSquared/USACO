with open("beads.in", "r") as f:
    totalbeads, necklace = f.read().split()

totalbeads = int(totalbeads)
high = 0
for i in range(1, totalbeads):
    j = 1
    total = 1
    w = None
    bead = necklace[i%totalbeads]
    while True:
        if necklace[(i-j)%totalbeads] in [bead, w]:
            j += 1
            total += 1
        else:
            break
        if "w" == bead:
            w = necklace[(i-j)%totalbeads]
        if "w" == necklace[(i-j)%totalbeads]:
            if bead != "w":
                w = bead
    j = 1
    i += 1
    w = None
    while True:
        if necklace[i%totalbeads] == necklace[(i+j)%totalbeads]:
            j += 1
            total += 1
        else:
            break
        if "w" == necklace[i%totalbeads]:
            w = necklace[(i+j)%totalbeads]
        if "w" == necklace[(i+j)%totalbeads]:
            w = necklace[i%totalbeads]
    print(total)
    if total > high:
        high = total
print(high)
