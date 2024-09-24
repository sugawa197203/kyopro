H, W = map(int, input().split())
posX, posY = map(int, input().split())
Grid = [list(input()) for _ in range(H)]
query = list(input())

for q in query:
	if q == "U":
		if posX > 1 and Grid[posX-2][posY-1] == ".":
			posX -= 1
	elif q == "D":
		if posX < H and Grid[posX][posY-1] == ".":
			posX += 1
	elif q == "L":
		if posY > 1 and Grid[posX-1][posY-2] == ".":
			posY -= 1
	elif q == "R":
		if posY < W and Grid[posX-1][posY] == ".":
			posY += 1
			
print(posX, posY)
