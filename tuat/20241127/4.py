N, M, K = map(int, input().split())

ans = 0

for i in range(M):
    pattern = 1
    maximam = minimum = i
    nextPattern = 2

    for j in range(N-1):
        maximam += K
        minimum -= K
        if maximam >= M:
            maximam = M - 1
