N = int(input())
Grid = [list(input()) for _ in range(N)]

def move(x, y, direct):
	if direct == "L":
		return (x, y - 1) if y > 0 else (x, N-1)
	elif direct == "R":
		return (x, y + 1) if y < N-1 else (x, 0)
	elif direct == "U":
		return (x - 1, y) if x > 0 else (N-1, y)
	elif direct == "D":
		return (x + 1, y) if x < N-1 else (0, y)
	elif direct == "LU":
		x, y = move(x, y, "L")
		return move(x, y, "U")
	elif direct == "LD":
		x, y = move(x, y, "L")
		return move(x, y, "D")
	elif direct == "RU":
		x, y = move(x, y, "R")
		return move(x, y, "U")
	elif direct == "RD":
		x, y = move(x, y, "R")
		return move(x, y, "D")

maximumNum = 0
for i in range(N):
	for j in range(N):
		for direct in ["L", "R", "U", "D", "LU", "LD", "RU", "RD"]:
			x, y = i, j
			num = ""	
			for k in range(N):
				num += str(Grid[x][y])
				x, y = move(x, y, direct)
			maximumNum = max(maximumNum, int(num))
print(maximumNum)
