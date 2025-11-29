N, M = map(int, input().split())

MM = [0] * (M + 1)
CMM = [0] * (M + 1)
for _ in range(N):
    A, B = map(int, input().split())
    MM[A] += B
    CMM[A] += 1

for i in range(1, M + 1):
    print(MM[i] / CMM[i])