H, W = map(int, input().split())
Grid = [list(input()) for _ in range(H)]

brackTop = 0
brackBottom = H
brackLeft = W
brackRight = 0

for i in range(H):
	for j in range(W):
		if Grid[i][j] == "#":
			brackTop = max(brackTop, i)
			brackBottom = min(brackBottom, i)
			brackLeft = min(brackLeft, j)
			brackRight = max(brackRight, j)

for i in range(H):
	for j in range(W):
		if Grid[i][j] == ".":
			if (brackBottom <= i <= brackTop) and (brackLeft <= j <= brackRight):
				print("No")
				exit()

print("Yes")
