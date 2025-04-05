H, W = map(int, input().split())
S = [list(input()) for _ in range(H)]
Sh, Sw, Gh, Gw = map(int, input().split())

Sh -= 1
Sw -= 1
Gh -= 1
Gw -= 1

from collections import deque

hq = deque()
hq.append((0, Sh, Sw))

grid = [[float("inf")] * W for _ in range(H)]
grid[Sh][Sw] = 0

while hq:
	cost, h, w = hq.popleft()
	if h == Gh and w == Gw:
		print(cost)
		break
	for dh, dw in ((1, 0), (-1, 0), (0, 1), (0, -1)):
		nh = h + dh
		nw = w + dw
		if 0 <= nh < H and 0 <= nw < W:
			if grid[nh][nw] > cost:
				if S[nh][nw] == '.':
					hq.appendleft((cost , nh, nw))
					grid[nh][nw] = cost
				else:
					hq.append((cost + 1, nh, nw))
					grid[nh][nw] = cost + 1

	for dh2, dw2 in ((2, 0), (-2, 0), (0, 2), (0, -2)):
		nh2 = h + dh2
		nw2 = w + dw2
		if 0 <= nh2 < H and 0 <= nw2 < W:
			if S[nh2][nw2] == '#':
				if grid[nh2][nw2] > cost + 1:
					grid[nh2][nw2] = cost + 1
					hq.append((cost + 1, nh2, nw2))
					
