N = int(input())
Grid = []
for i in range(N):
	Grid.append(input())
ansgrid = [['.' for _ in range(N)] for _ in range(N)]
mid = N//2
for i in range(N//2):
	rot = i % 4
	for j in range(N - i*2 - 1):
		if rot == 0:
			ansgrid[i][j + i] = Grid[N - i - j - 1][i]
			ansgrid[j + i][N - i - 1] = Grid[i][j + i]
			ansgrid[N - i - 1][N - i - j - 1] = Grid[j + i][N - i - 1]
			ansgrid[N - i - j - 1][i] = Grid[N - i - 1][N - i - j - 1]
		elif rot == 1:
			ansgrid[j + i][N - i - 1] = Grid[N - i - j - 1][i]
			ansgrid[N - i - 1][N - i - j - 1] = Grid[i][j + i]
			ansgrid[N - i - j - 1][i] = Grid[j + i][N - i - 1]
			ansgrid[i][j + i] = Grid[N - i - 1][N - i - j - 1]
		elif rot == 2:
			ansgrid[N - i - 1][N - i - j - 1] = Grid[N - i - j - 1][i]
			ansgrid[N - i - j - 1][i] = Grid[i][j + i]
			ansgrid[i][j + i] = Grid[j + i][N - i - 1]
			ansgrid[j + i][N - i - 1] = Grid[N - i - 1][N - i - j - 1]
		elif rot == 3:
			ansgrid[N - i - j - 1][i] = Grid[N - i - j - 1][i]
			ansgrid[i][j + i] = Grid[i][j + i]
			ansgrid[j + i][N - i - 1] = Grid[j + i][N - i - 1]
			ansgrid[N - i - 1][N - i - j - 1] = Grid[N - i - 1][N - i - j - 1]
		

for i in range(N):
	print(''.join(ansgrid[i]))

