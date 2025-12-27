from collections import deque

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

A_acc = [0] * (N + 1)
for i in range(N):
    A_acc[i + 1] = A_acc[i] + A[i]
B_acc = [0] * (N + 1)
for i in range(N):
    B_acc[i + 1] = B_acc[i] + B[i]
C_acc = [0] * (N + 1)
for i in range(N):
    C_acc[i + 1] = C_acc[i] + C[i]

nowmax = -float("inf")
max_val = [-float("inf")] * (N + 1)
for i in range(1, N):
    nowmax = max(nowmax, A_acc[i] - B_acc[i])
    max_val[i] = nowmax


ans = 0
for y in range(2, N):
    val = B_acc[y] + (C_acc[N] - C_acc[y]) + max_val[y - 1]
    ans = max(ans, val)

print(ans)
