X, Y = input().split()
V = ["Ocelot", "Serval", "Lynx"]

xin = V.index(X)
yin = V.index(Y)

if xin >= yin:
    print("Yes")
else:
    print("No")
