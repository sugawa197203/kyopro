N, M = map(int, input().split())

place = set()

for _ in range(M):
	r, c = map(int, input().split())
	rcs = [(r, c), (r+1, c), (r, c+1), (r+1, c+1)]
	if all(rc not in place for rc in rcs):
		place.update(rcs)

print(len(place) // 4)