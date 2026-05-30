T = int(input())

from math import sqrt

for _ in range(T):
    X1, Y1, R1, X2, Y2, R2 = map(int, input().split())

    bigx1, bigy1, bigr1 = (X1, Y1, R1) if R1 > R2 else (X2, Y2, R2)
    smallx1, smally1, smallr1 = (X2, Y2, R2) if R1 > R2 else (X1, Y1, R1)

    dist = (X1 - X2) ** 2 + (Y1 - Y2) ** 2

    # utigawakadouka
    # print(smallr1 ** 2 + dist, bigr1 ** 2)
    if smallr1 + sqrt(dist) < bigr1:
        print("No")
        continue
    if dist <= (R1 + R2) ** 2:
        print("Yes")
    else:
        print("No")
