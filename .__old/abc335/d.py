N = int(input())

grid = []
for i in range(N):
	line = []
	for j in range(N):
		line.append(00)
	grid.append(line)


direction = (0, 1)
pos = (0, 0)
length = N - 1
roop = (N - 1) // 2
count = 0

for i in range(roop):
	direction = (0, 1)
	for j in range(length):
		count += 1
		grid[pos[0]][pos[1]] = count
		pos = (pos[0] + direction[0], pos[1] + direction[1])
	
	direction = (1, 0)
	for j in range(length):
		count += 1
		grid[pos[0]][pos[1]] = count
		pos = (pos[0] + direction[0], pos[1] + direction[1])
	
	direction = (0, -1)
	for j in range(length):
		count += 1
		grid[pos[0]][pos[1]] = count
		pos = (pos[0] + direction[0], pos[1] + direction[1])
	
	direction = (-1, 0)
	for j in range(length):
		count += 1
		grid[pos[0]][pos[1]] = count
		pos = (pos[0] + direction[0], pos[1] + direction[1])
	
	length -= 2
	pos = (pos[0] + 1, pos[1] + 1)

for i in range(N):
	for j in range(N):
		if i == (N - 1) // 2 and j == (N - 1) // 2:
			print("T", end=" ")
		else:
			print(grid[i][j], end=" ")
	print()
	