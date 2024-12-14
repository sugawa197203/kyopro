H, W, D = map(int, input().split())
Grid = [list(input()) for _ in range(H)]

ans = [[False] * W for _ in range(H)]
memo = [[0] * W for _ in range(H)]
for y in range(H):
	for x in range(W):
		if Grid[y][x] == "H":
			ans[y][x] = True
			# mark = set()
			que = [(y, x, D)]
			memo[y][x] = D + 1
			while que:
				_y, _x, d = que.pop(0)
				for dy, dx in ((0, 1), (1, 0), (0, -1), (-1, 0)):
					ny, nx = _y + dy, _x + dx
					if 0 <= ny < H and 0 <= nx < W and Grid[ny][nx] == "." and d > 0 and memo[ny][nx] < d:
						# if (ny, nx) in mark:
						# 	continue
						memo[ny][nx] = d
						ans[ny][nx] = True
						que.append((ny, nx, d-1))
						# mark.add((ny, nx))
						
			# print("\n".join(",".join(str(memo[y][x]) for x in range(W)) for y in range(H)))
			# print()
anscount = sum(sum(row) for row in ans)
print(anscount)

