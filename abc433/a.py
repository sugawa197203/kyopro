X, Y, Z = map(int, input().split())

for i in range(1, 10000):
    if Y * Z == X:
        print("Yes")
        exit()
    X += 1
    Y += 1

print("No")
