"""
ID: vishvib1
LANG: PYTHON3
PROB: mixmilk
"""

fin = open("mixmilk.in", "r")
a, b, c, _ = [s.split() for s in fin.read().split("\n")]
fin.close()
buckets = [int(a[1]), int(b[1]), int(c[1])]
max = [int(a[0]), int(b[0]), int(c[0])]
bucket = ["a", "b", "c"]
for i in range(100):
    cb = i%3
    nb = (i+1)%3
    if buckets[cb] < (max[nb] - buckets[nb]):
        buckets[nb] += buckets[cb]
        buckets[cb] = 0
    else:
        temp = buckets[nb]
        buckets[nb] = max[nb]
        buckets[cb] = buckets[cb] - max[nb] + temp

fout = open("mixmilk.out", "w")
fout.write("\n".join(str(i) for i in buckets))
fout.close()