H, W = map(int, input().split())
G = [input() for _ in range(H)]

for i in range(H):
    for j in range(W):
        if G[i][j] == ".":
            continue

        count = 0
        for di, dj in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            ni, nj = i + di, j + dj
            if 0 <= ni < H and 0 <= nj < W and G[ni][nj] == "#":
                count += 1

        if not (count == 2 or count == 4):
            print("No")
            exit()

print("Yes")
