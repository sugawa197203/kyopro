H, W = map(int, input().split())

ans = [[4] * W for _ in range(H)]

for i in range(H):
    for j in range(W):
        if i == 0:
            ans[i][j] -= 1
        if i == H - 1:
            ans[i][j] -= 1
        if j == 0:
            ans[i][j] -= 1
        if j == W - 1:
            ans[i][j] -= 1

for i in range(H):
    print(*ans[i])
