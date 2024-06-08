N = int(input())
if N == 0:
	print("#")
	exit()
grid = [["." for _ in range(3 ** N)] for _ in range(3 ** N)]

def draw(x, y, n, _grid):
	if n == 1:
		for i in range(3):
			for j in range(3):
				_grid[x + i][y + j] = "." if i == 1 and j == 1 else "#"
		return
	
	_n = n // 3
	for i in range(3):
		for j in range(3):

			if i == 1 and j == 1:
				for _i in range(_n):
					for _j in range(_n):
						_grid[x + _i + _n][y + _j + _n] = "."
			else:
				
				draw(x + i * (3 ** (n - 1)), y + j * (3 ** (n - 1)), n - 1, _grid)
				

draw(0, 0, N, grid)
for row in grid:
	print("".join(row))
