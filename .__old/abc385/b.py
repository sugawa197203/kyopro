H, W, X, Y = map(int, input().split())
Grid = [list(input()) for _ in range(H)]
T = input()

pos = (X - 1, Y - 1)
through = set()

if Grid[pos[0]][pos[1]] == "@":
	through.add(pos)

for t in T:
	if t == "U":
		if pos[0] > 0 and Grid[pos[0] - 1][pos[1]] != "#":
			pos = (pos[0] - 1, pos[1])
	elif t == "D":
		if pos[0] < H - 1 and Grid[pos[0] + 1][pos[1]] != "#":
			pos = (pos[0] + 1, pos[1])
	elif t == "L":
		if pos[1] > 0 and Grid[pos[0]][pos[1] - 1] != "#":
			pos = (pos[0], pos[1] - 1)
	elif t == "R":
		if pos[1] < W - 1 and Grid[pos[0]][pos[1] + 1] != "#":
			pos = (pos[0], pos[1] + 1)

	if Grid[pos[0]][pos[1]] == "@":
		through.add(pos)

print(pos[0]+1, pos[1]+1, len(through))
