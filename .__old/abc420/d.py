from heapq import heappop, heappush

H, W = map(int, input().split())

Grid = [input() for _ in range(H)]
watched = {True: [[False] * W for _ in range(H)], False: [[False] * W for _ in range(H)]}

pos = (0, 0)
for i in range(H):
    for j in range(W):
        if Grid[i][j] == "S":
            pos = (i, j)
            break

q = [(0, (pos[0], pos[1], True))]
watched[True][pos[0]][pos[1]] = True

while q:
    cost, (x, y, state) = heappop(q)
    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < H and 0 <= ny < W:
            if Grid[nx][ny] == "#":
                continue
            if Grid[nx][ny] == "G":
                print(cost + 1)
                exit()
            if Grid[nx][ny] == "?":
                if watched[not state][nx][ny]:
                    continue
                heappush(q, (cost + 1, (nx, ny, not state)))
                watched[not state][nx][ny] = True
                continue
            if watched[state][nx][ny]:
                continue
            if Grid[nx][ny] == "x" and state:
                continue
            if Grid[nx][ny] == "o" and not state:
                continue
            heappush(q, (cost + 1, (nx, ny, state)))
            watched[state][nx][ny] = True
            
print(-1)

