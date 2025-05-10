from collections import deque
H, W = map(int, input().split())
Grid = [list(input()) for _ in range(H)]

Directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def strByDir(a, b):
	d = (a[0] - b[0], a[1] - b[1])
	if d[0] == 1 and d[1] == 0:
		return '^'
	if d[0] == 0 and d[1] == 1:
		return '<'
	if d[0] == -1 and d[1] == 0:
		return 'v'
	if d[0] == 0 and d[1] == -1:
		return '>'

ans = Grid

start = []

for h in range(H):
	for w in range(W):
		if Grid[h][w] == 'E':
			start.append((h, w))

if not start:
	for h in range(H):
		print(''.join(ans[h]))
	exit(0)

def get_next(pos, _from):
	h, w = pos
	retval = []
	for dh, dw in Directions:
		if 0 <= h + dh < H and 0 <= w + dw < W:
			if h + dh == _from[0] and w + dw == _from[1]:
				continue
			if Grid[h + dh][w + dw] not in '#E':
				retval.append((h + dh, w + dw))
	return retval

queue = [(s, f) for s, f in zip(start, start)]
queue = deque(queue)

while queue:
	pos, _from = queue.popleft()
	for _next in get_next(pos, _from):
		if ans[_next[0]][_next[1]] == '.':
			ans[_next[0]][_next[1]] = strByDir(_next, pos)
			queue.append((_next, pos))

for h in range(H):
	print(''.join(ans[h]))
