a = int(input())
b = int(input())
c = int(input())
d = int(input())
sred = round((a*5+b*4+c*3+d*2)/(a+b+c+d))
if sred > 4:
    print(a)
elif sred > 3:
    print(a+b)
elif sred > 2:
    print(a + b + c)
