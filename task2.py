f = open('26-145.txt')
n = int(f.readline())
m, k = map(int, f.readline().split())
a = [[int(y) for y in x.split()] for x in f]
a.sort(reverse=True)
carriages = [[k, k, k * 6] for i in range(m)]
current = 0
children = 0
for i in range(n):
    if a[i][0] < 3 and a[i - 1][0] > 2:
        current = 0
    if current < m:
        carriages[current][2] -= a[i][0]
        children += a[i][1]
        if a[i][0] > 2:
            carriages[current][0] -= 1
            if carriages[current][0] == 0:
                current += 1
        else:
            carriages[current][1] -= 1
            if carriages[current][1] == 0:
                current += 1
mxi = 0
for i in range(1, m):
    if carriages[i][2] > carriages[mxi][2]:
        mxi = i
print(children, mxi + 1)