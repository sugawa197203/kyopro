H, W = map(int, input().split())
S = [list(input()) for _ in range(H)]

maxinum = 0

watched = [[0] * W for _ in range(H)]
note = []

for h in range(H):
	for w in range(W):
		if S[h][w] == "#":
			continue

		if watched[h][w] == 1:
			continue

		watched[h][w] = 1
		count = 1

		# bfs
		queue = [(h, w)]
		while queue:
			h, w = queue.pop(0)
			flag = False
			for dh, dw in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
				nh, nw = h + dh, w + dw
				if nh < 0 or nh >= H or nw < 0 or nw >= W:
					continue
				if S[nh][nw] == "#":
					flag = True
					note.append((h, w))
					break

			if flag:
				continue

			for dh, dw in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
				nh, nw = h + dh, w + dw
				if nh < 0 or nh >= H or nw < 0 or nw >= W:
					continue
				if watched[nh][nw] == 1:
					continue

				watched[nh][nw] = 1
				count += 1
				queue.append((nh, nw))
		
		while note:
			h, w = note.pop()
			watched[h][w] = 0
		maxinum = max(maxinum, count)

print(maxinum)