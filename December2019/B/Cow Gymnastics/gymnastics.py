"""
ID: piaresquared
LANG: PYTHON3
PROB: gymnastics
"""

fin = open("gymnastics.in", "r")
k, n = [int(i) for i in fin.readline().replace("\n", "").split()]
sessions = [[None]*n for i in range(k)]
consistant = 0
con = True

for i in range(k):
    cows = fin.readline().replace("\n", "").split()
    for cow in cows:
        sessions[i][int(cow)-1] = int(cows.index(cow))

for cow1 in range(0, n):
    for cow2 in range(cow1+1, n):
        con = True
        if sessions[0][cow1] > sessions[0][cow2]:
            better = cow1
            worse = cow2
        if sessions[0][cow1] < sessions[0][cow2]:
            better = cow2
            worse = cow1
        for i in range(1, len(sessions)):
            if not((sessions[i][better] > sessions[i][worse])):
                con = False
        if con:
            consistant += 1

consistant = str(consistant)

fout = open("gymnastics.out", "w+")
fout.write(consistant)
fout.close()