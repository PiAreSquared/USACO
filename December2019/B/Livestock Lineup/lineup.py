"""
ID: piaresquared
LANG: PYTHON3
PROB: lineup
"""

fin = open("lineup.in", "r")
n = int(fin.readline().replace("\n", ""))
lists = []

def printLists(lists):
    for li in lists:
        print(li)

def isHeadofList(a, li):
    return a == li[0]
def isTailofList(a, li):
    return a == li[-1]
def isHeadorTailofList(a, li):
    return a == li[0] or a == li[-1]

def inAnyPositionofLists(a, lists):
    for li in lists:
        if a in li:
            return True
    return False

def inLists(a, lists):
    for li in lists:
        if isHeadorTailofList(a, li):
            return True
    return False

def insertIntoaList(a, b, li):
    if a == li[0]:
        li.insert(0, b)
    elif a == li[-1]:
        li.append(b)
    elif b == li[0]:
        li.insert(0, a)
    elif b == li[-1]:
        li.append(a)

def mergeList(a, b, aa, bb):
    if not isTailofList(a, aa):
        aa.reverse()
    if not isHeadofList(b, bb):
        bb.reverse()
    return aa + bb

def insertIntoLists(a, b, lists):
    a_in_lists = inLists(a, lists)
    b_in_lists = inLists(b, lists)
    one_and_only_one_in_lists = (a_in_lists + b_in_lists) == 1
    if (not a_in_lists) and (not b_in_lists):
        lists.append([a, b])
        return
    elif one_and_only_one_in_lists:
        for li in lists:
            insertIntoaList(a, b, li)
        return
    aa = []
    bb = []
    for li in lists:
        if isHeadorTailofList(a, li):
            aa = li
        if isHeadorTailofList(b, li):
            bb = li
    lists.remove(aa)
    lists.remove(bb)
    aabb = mergeList(a, b, aa, bb)
    lists.append(aabb)


for line in range(n):
    words = fin.readline().replace("\n", "").split()
    a = words[0]
    b = words[5]
    insertIntoLists(a, b, lists)

for name in ['Bessie', 'Buttercup', 'Belinda', 'Beatrice', 'Bella', 'Blue', 'Betsy', 'Sue']:
    if not inAnyPositionofLists(name, lists):
        lists.append([name])

def sortList(aa):
    if aa[0] > aa[-1]:
        aa.reverse()

for aa in lists:
    sortList(aa)

lists = sorted(lists, key=lambda x: x[0])

order = []

for li in lists:
    for a in li:
        order.append(a)


fout = open("lineup.out", "w")
fout.write("\n".join(str(i) for i in order))
fout.close()