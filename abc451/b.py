N, M = map(int, input().split())

AB = [tuple(map(int, input().split())) for _ in range(N)]

A = [0] * M
B = [0] * M

for i in range(N):
    a, b = AB[i]
    A[a-1] += 1
    B[b-1] += 1

for i in range(M):
    print(B[i] - A[i])
