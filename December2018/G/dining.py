import sys
import time

"""
ID: vishvib1
LANG: PYTHON3
PROB: dining
"""

fin = open("dining.in", "r")
map = {}
yummy = {}
N, M, K = [int(i) for i in fin.readline().split()]
for i in range(M):
    a, b, t = [int(i) for i in fin.readline().split()]
    if a in map:
        if b in map[a]:
            if map[a][b] > t:
                map[a][b] = t 
        else:
            map[a][b] = t
    else:
        map[a] = {}
        map[a][b] = t
    if b in map:
        if a in map[b]:
            if map[b][a] > t:
                map[b][a] = t 
        else:
            map[b][a] = t
    else:
        map[b] = {}
        map[b][a] = t

for i in range(K):
    index, y = [int(i) for i in fin.readline().split()]
    yummy[index] = y

def findLeast(a, b, emap=map, previous=[]):
    lmap = emap[a]
    least = sys.maxsize
    if b in lmap:
        least = lmap[b]
    previous.append(a)
    if previous + [b] == lmap.keys():
        return lmap[b]
    if a == b:
        return 0
    for i in lmap:
        if i in previous:
            continue
        elif lmap[i] < least:
            l = findLeast(i, b, emap, previous)
            if lmap[i] + l < least:
                least = lmap[i] + l
    return least

print(findLeast())

# out = []
# for i in range(1, N):
#     one = False
#     for index in yummy:
#         if findLeast(i, index) + findLeast(index, N) - findLeast(i, N) <= yummy[index]:
#             one = True
#     out.append("1" if one else "0")
# 
# fout = open("dining.out", "w+")
# 
# fout.write("\n".join(out))