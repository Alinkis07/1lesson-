s = open('24-264.txt').readline()
k = 1
mx = 1
d = '0123456789'
for i in range(1, len(s)):
    if (s[i] in d) != (s[i - 1] in d):
        k += 1
        mx = max(mx, k)
    else:
        k = 1
print(mx)