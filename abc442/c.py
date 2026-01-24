N, M = map(int, input().split())

rigaicount = [0] * N

for _ in range(M):
    a, b = map(int, input().split())
    rigaicount[a - 1] += 1
    rigaicount[b - 1] += 1

ans = [0] * N

for i in range(N):
    sadoku = N - rigaicount[i] - 1
    if sadoku < 3:
        ans[i] = 0
    else:
        ans[i] = sadoku * (sadoku - 1) * (sadoku - 2) // 6

print(*ans)
