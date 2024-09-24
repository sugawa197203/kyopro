H, W = map(int, input().split())
Grid = [[0] * (W + 2) for _ in range(H + 2)]

for i in range(1, H + 1):
	Grid[i][1:W + 1] = list(input())

for i in range(1, H + 1):
	for j in range(1, W + 1):
		if Grid[i][j] == "#":
			continue
		count = 0
		for dx in range(-1, 2):
			for dy in range(-1, 2):
				if Grid[i + dx][j + dy] == "#":
					count += 1
		Grid[i][j] = str(count)

for i in range(1, H + 1):
	print("".join(Grid[i][1:W + 1]))