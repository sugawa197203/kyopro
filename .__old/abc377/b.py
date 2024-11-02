S = []
for i in range(8):
	S.append(list(input()))
ans = [[0] * 8 for i in range(8)]
for i in range(8):
	for j in range(8):
		if S[i][j] == '#':
			ans[i][j] = 1
			for d in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
				for k in range(1, 8):
					nx = i + d[0] * k
					ny = j + d[1] * k
					if nx < 0 or nx >= 8 or ny < 0 or ny >= 8:
						break
					ans[nx][ny] = 1

zerocount = 0
for i in range(8):
	for j in range(8):
		if ans[i][j] == 0:
			zerocount += 1

print(zerocount)				
