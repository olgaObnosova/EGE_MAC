sp = [0] * 10_005
for i in range(10_004, -1, -1):
    if i >= 10_000:
        sp[i] = i
    elif i % 2 == 0:
        sp[i] = sp[i + 2] - 3
    else:
        sp[i] = sp[i + 2] + 1
print(sp[94] - sp[80])
