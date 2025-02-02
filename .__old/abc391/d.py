N, W = map(int, input().split())
# pos[0] = x, pos[1] = y
pos = [list(map(int, input().split())) for _ in range(N)]
Q = int(input())
import bisect
posSortedByY = list(range(N))
posSortedByY = sorted(posSortedByY, key=lambda x: pos[x][1])
posSortedByX = list(range(N))
posSortedByX = sorted(posSortedByX, key=lambda x: pos[x][0])
lifetimeByBlock = [10**9+1] * N

linecount = 0
stock = [0] * W
beforetime = 1
stockblocks:list[list] = []
for i in range(W):
	stockblocks.append([])

for i in range(N):
	time = pos[posSortedByY[i]][1]
	stock[pos[posSortedByY[i]][0] - 1] += 1
	stockblocks[pos[posSortedByY[i]][0] - 1].append(posSortedByY[i])
	if stock[pos[posSortedByY[i]][0] - 1] == 1:
		linecount += 1
	beforetime = time
	# print()
	# print(f"line time: {time}")
	# print(f"stock: {stock}")
	# print(f"stockblocks: {stockblocks}")
	if linecount == W:
		for i in range(W):
			id = stockblocks[i].pop(0)
			lifetimeByBlock[id] = time
			stock[i] -= 1
		linecount = 0

		for i in range(W):
			if len(stockblocks[i]) > 0:
				linecount += 1

# print(lifetimeByBlock)
for i in range(Q):
	t, id = map(int, input().split())
	id -= 1
	if lifetimeByBlock[id] > t:
		print("Yes")
	else:
		print("No")