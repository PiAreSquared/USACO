"""
ID: piaresquared
LANG: PYTHON3
PROB: whereami
"""

fin = open("whereami.in", "r")
n = int(fin.readline())
chars = list(fin.readline().replace("\n", ""))
ch = {}
for i in range(0, n):
    for j in range(i+1, n+1):
        val = "".join(chars[i:j])
        ch[len(val)] = {val} if len(val) not in ch else ch[len(val)].union({val})

for i in range(1, n+1):
    if len(ch[i]) == n+1-i:
        out = str(i)
        break

fout = open("whereami.out", "w")
fout.write(out)
fout.close()