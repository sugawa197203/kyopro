from collections import deque, defaultdict

H, W = map(int, input().split())

dx = [(1, 0) , (0, 1), (-1, 0), (0, -1)]
watched = [[False] * W for _ in range(H)]

G = [list(input()) for _ in range(H)]

start = (0, 0)
q = deque([(start, 0, False)])
watched[0][0] = True
warp = defaultdict(list)

for i in range(H):
	for j in range(W):
		if G[i][j] != "#" and G[i][j] != ".":
			alpha = G[i][j]
			warp[alpha].append((i, j))

while q:
	(x, y), dist, usedwarp = q.popleft()

	if (x, y) == (H-1, W-1):
		break

	if not usedwarp and G[x][y] != "#" and G[x][y] != ".":
		alpha = G[x][y]
		for wx, wy in warp[alpha]:
			if not watched[wx][wy]:
				watched[wx][wy] = True
				q.append(((wx, wy), dist + 1, True))
		warp[alpha] = []
	
	for dx_i, dy_i in dx:
		nx, ny = x + dx_i, y + dy_i
		if 0 <= nx < H and 0 <= ny < W and not watched[nx][ny] and G[nx][ny] != '#':
			watched[nx][ny] = True
			q.append(((nx, ny), dist + 1, False))

if watched[H-1][W-1]:
	print(dist)
else:
	print("-1")
	