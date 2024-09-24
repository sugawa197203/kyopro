H, W, N = map(int, input().split())

Grid = [["." for __ in range(W)] for _ in range(H)]

x, y = 0, 0

directionX = 0
directionY = 1

for _ in range(N):

	if "." == Grid[y][x]:
		Grid[y][x] = "#"
		directionX, directionY = directionY, -directionX
		x = (x + directionX) % W
		y = (y - directionY) % H
	else:
		Grid[y][x] = "."
		directionX, directionY = -directionY, directionX
		x = (x + directionX) % W
		y = (y - directionY) % H

for row in Grid:
	print("".join(row))
