f = open('24-164.txt')
a = f.readlines()
abc = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
c = 0
mx = 0
mxs = ''
for s in a:
    for l in abc:
        ts = l
        while ts in s:
            if len(ts) > mx:
                mx = len(ts)
                mxs = s
            ts += l
mn = 10**10
mnl = ''
for l in abc:
    if mxs.count(l) <= mn:
        mn = mxs.count(l)
        mnl = l
for s in a:
    c += s.count(mnl)
print(mnl, c)