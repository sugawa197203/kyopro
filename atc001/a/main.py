H, W = map(int, input().split())

start, goal = (0, 0), (0, 0)

C = [list(input()) for _ in range(H)]

for i in range(H):
	for j in range(W):
		if C[i][j] == "s":
			start = (i, j)
		if C[i][j] == "g":
			goal = (i, j)

visited = [[False]*W for _ in range(H)]
stack = [start]
while stack:
	y, x = stack.pop()
	if visited[y][x]:
		continue
	visited[y][x] = True
	for dy, dx in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
		ny, nx = y + dy, x + dx
		if 0 <= ny < H and 0 <= nx < W and not visited[ny][nx] and C[ny][nx] != "#":
			stack.append((ny, nx))
if visited[goal[0]][goal[1]]:
	print("Yes")
else:
	print("No")
