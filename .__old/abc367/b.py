F = float(input())
I = int(F * 1000)
if I == 0:
    print(0)
elif I % 1000 == 0:
    print(I // 1000)
else:
    print(I / 1000)