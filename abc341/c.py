H, W, N = map(int, input().split())
T = input()
S = [input() for _ in range(H)]

count = 0
for h in range(1, H - 1):
	for w in range(1, W - 1):
		if S[h][w] == "#":
			continue
		
		pos = (h, w)
		f = False
		for t in T:
			if t == "L" and S[pos[0]][pos[1] - 1] != "#":
				pos = (pos[0], pos[1] - 1)
			elif t == "R" and S[pos[0]][pos[1] + 1] != "#":
				pos = (pos[0], pos[1] + 1)
			elif t == "U" and S[pos[0] - 1][pos[1]] != "#":
				pos = (pos[0] - 1, pos[1])
			elif t == "D" and S[pos[0] + 1][pos[1]] != "#":
				pos = (pos[0] + 1, pos[1])
			else:
				f = True
				break

		if not f:
			count += 1

print(count)	
		