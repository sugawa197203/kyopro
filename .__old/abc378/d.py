H, W, K = map(int, input().split())
S = []
for i in range(H):
	S.append(list(input()))
count = 0

def get_neighbors(pos) -> list:
	neighbors = []
	for dx, dy in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
		if 0 <= pos[0] + dx < H and 0 <= pos[1] + dy < W:
			if S[pos[0] + dx][pos[1] + dy] == '.':
				neighbors.append((pos[0] + dx, pos[1] + dy))
	return neighbors

def dfs(start, visited:set, step):
	global count
	if step == K:
		count += 1
		return
	for neighbor in get_neighbors(start):
		if neighbor in visited:
			continue
		visited.add(neighbor)
		dfs(neighbor, visited, step + 1)
		visited.remove(neighbor)

for i in range(H):
	for j in range(W):
		if S[i][j] == '#':
			continue
		start = (i, j)
		visited = set()
		visited.add(start)
		dfs(start, visited, 0)

print(count)