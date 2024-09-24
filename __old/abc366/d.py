N = int(input())
A = [[list(map(int, input().split())) for _ in range(N)] for _ in range(N)]

Aruisekiwa = [[[0 for _ in range(N)] for _ in range(N)] for _ in range(N)]


for i in range(N):
    for j in range(N):
        for k in range(N):
            if k == 0:
                Aruisekiwa[i][j][k] = A[i][j][0]
            else:
                Aruisekiwa[i][j][k] = Aruisekiwa[i][j][k-1] + A[i][j][k]

for i in range(N):
    for j in range(N):
        for k in range(N):
            if k == 0:
                Aruisekiwa[i][k][j] = Aruisekiwa[i][0][j]
            else:
                Aruisekiwa[i][k][j] = Aruisekiwa[i][k-1][j] + Aruisekiwa[i][k][j]

for i in range(N):
    for j in range(N):
        for k in range(N):
            if k == 0:
                Aruisekiwa[k][i][j] = Aruisekiwa[0][i][j]
            else:
                Aruisekiwa[k][i][j] = Aruisekiwa[k-1][i][j] + Aruisekiwa[k][i][j]
Q = int(input())
for _ in range(Q):
    Lx, Rx, Ly, Ry, Lz, Rz = map(int, input().split())
    Lx -= 1
    Rx -= 1
    Ly -= 1
    Ry -= 1
    Lz -= 1
    Rz -= 1

    zenbu = Aruisekiwa[Rx][Ry][Rz]
    if Lx > 0:
        zenbu -= Aruisekiwa[Lx-1][Ry][Rz]
    if Ly > 0:
        zenbu -= Aruisekiwa[Rx][Ly-1][Rz]
    if Lz > 0:
        zenbu -= Aruisekiwa[Rx][Ry][Lz-1]
    if Lx > 0 and Ly > 0:
        zenbu += Aruisekiwa[Lx-1][Ly-1][Rz]
    if Lx > 0 and Lz > 0:
        zenbu += Aruisekiwa[Lx-1][Ry][Lz-1]
    if Ly > 0 and Lz > 0:
        zenbu += Aruisekiwa[Rx][Ly-1][Lz-1]
    if Lx > 0 and Ly > 0 and Lz > 0:
        zenbu -= Aruisekiwa[Lx-1][Ly-1][Lz-1]
    
    print(zenbu)
    
