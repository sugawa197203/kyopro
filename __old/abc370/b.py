N = int(input())

A = []

for i in range(N):
    A.append(list(map(int, input().split())))
now = 0

for i in range(N):
    if now >= i:
        now = A[now][i] - 1
    else:
        now = A[i][now] - 1

print(now+1)