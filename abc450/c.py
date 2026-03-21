H, W = map(int, input().split())
S = [input() for _ in range(H)]

watched = [[False] * W for _ in range(H)]

ans = 0

for i in range(H):
    for j in range(W):
        if watched[i][j]:
            continue
        if S[i][j] == "#":
            continue
        stack = [(i, j)]
        outflag = i == 0 or i == H - 1 or j == 0 or j == W - 1
        while stack:
            x, y = stack.pop()
            watched[x][y] = True
            for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nx, ny = x + dx, y + dy
                if not (0 <= nx < H and 0 <= ny < W):
                    continue
                if S[nx][ny] == "#":
                    continue
                if watched[nx][ny]:
                    continue
                if nx == 0 or nx == H - 1 or ny == 0 or ny == W - 1:
                    outflag = True
                stack.append((nx, ny))
        if not outflag:
            ans += 1

print(ans)
