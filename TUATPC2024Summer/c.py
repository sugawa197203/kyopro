N, M = input().split()
N = int(N)
M = int(M[-2:])

A = []
for i in range(N):
    A.append([0] * N)

for i in range(N):
    for j in range(N):
        A[i][j] = (M + i) * (M + j) % 100

for a in A:
    for _a in a:
        print(str(_a).zfill(2), end=" ")
    print("")
