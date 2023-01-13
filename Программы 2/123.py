n = int(input())
f1 = 0
f2 = 1
for i in range(n-2):
    f = f1 + f2
    f1 = f2
    f2 = f

print(f)
    
