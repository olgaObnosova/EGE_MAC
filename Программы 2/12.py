f=open('17.txt')
sp=[]
kol100=0
k=0
maxx=0
for line in f:
    line=int(line)
    sp.append(line)
    if abs(line)<100:
        kol100+=1
for i in range(len(sp)-1):
    if (sp[i]+sp[i+1])/2>kol100:
        k+=1
        maxx=max(maxx,sp[i]+sp[i+1])
print(k)
print(maxx)
