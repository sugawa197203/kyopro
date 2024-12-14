H, W, D = map(int, input().split())
Grid = [list(input()) for _ in range(H)]
maxans = 0

for x1 in range(H):
	for y1 in range(W):
		if Grid[x1][y1] == "#":
			continue
		for x2 in range(H):
			for y2 in range(W):
				if x1 == x2 and y1 == y2:
					continue
				if Grid[x2][y2] == "#":
					continue

				mark = [[False for _ in range(W)] for _ in range(H)]
				count = 0
				for x in range(H):
					for y in range(W):
						if Grid[x][y] == ".":
							manhattan = abs(x - x1) + abs(y - y1)
							if manhattan <= D:
								mark[x][y] = True
								count += 1
							manhattan = abs(x - x2) + abs(y - y2)
							if manhattan <= D and not mark[x][y]:
								mark[x][y] = True
								count += 1
				maxans = max(maxans, count)

print(maxans)