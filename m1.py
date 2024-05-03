s = open('24-253.txt').readline()
k = 0
a=[]
j=0
s = s.replace('C', '1').replace('D', '1').replace('F', '1').replace('A', '0').replace('O', '0')
s=s.replace('110','.').replace('100','.')
while j<len(s):
    if s[j] == '.':
        k+=1
    else:
        a.append(k)
        k=0
    j+=1
print(max(a))