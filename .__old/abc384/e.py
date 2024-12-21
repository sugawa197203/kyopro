import sortedcontainers

H, W, X = map(int, input().split())
P, Q = map(int, input().split())
P, Q = P - 1, Q - 1

Grid = [list(map(int, input().split())) for _ in range(H)]

done = {}
tonariSorted = sortedcontainers.SortedList(key=lambda x: x[1])

for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
	if not (0 <= P + dx < H and 0 <= Q + dy < W):
		continue
	v = Grid[P + dx][Q + dy]
	done[(dx + P, dy + Q)] = v
	tonariSorted.add(((dx + P, dy + Q), v))

ans = Grid[P][Q]
done[(P, Q)] = ans

while True:
	_x = ans/X

	lefti = tonariSorted.bisect_left((0, _x))
	if lefti == 0:
		break

	ind = lefti - 1
	(x, y), v = tonariSorted[ind]
	tonariSorted.pop(ind)
	ans += v

	for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
		if not (0 <= dx + x < H and 0 <= dy + y < W):
			continue
		if (dx + x, dy + y) in done:
			continue
		v = Grid[x + dx][y + dy]
		done[(dx + x, dy + y)] = v
		tonariSorted.add(((dx + x, dy + y), v))

print(ans)
