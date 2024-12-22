N, M , posx, posy = map(int, input().split())
X, Y = [0] * N, [0] * N
for i in range(N):
	X[i], Y[i] = map(int, input().split())
D, C = [0] * M, [0] * M
for i in range(M):
	d, c = input().split()
	D[i], C[i] = d, int(c)

import collections
import sortedcontainers
homeX = collections.defaultdict(sortedcontainers.SortedList)
homeY = collections.defaultdict(sortedcontainers.SortedList)
ans = N

for i in range(N):
	homeX[X[i]].add(Y[i])
	homeY[Y[i]].add(X[i])

# if posx in homeX:
# 	left = homeX[posx].bisect_left(posy)
# 	if posy == homeX[posx][left]:
# 		ans -= 1
# 		y = homeX[posx].pop(left)
# 		homeY[y].remove(posx)
# 		if len(homeY[y]) == 0:
# 			del homeY[y]
# 		if len(homeX[posx]) == 0:
# 			del homeX[posx]

for d, c in zip(D, C):
	if d == "U":
		old = posy
		posy += c
		if posx in homeX:
			left = homeX[posx].bisect_left(old)
			right = homeX[posx].bisect_left(posy)
			ans -= right - left
			for i in range(left, right):
				y = homeX[posx].pop(left)
				homeY[y].remove(posx)
				if len(homeY[y]) == 0:
					del homeY[y]
				if len(homeX[posx]) == 0:
					del homeX[posx]
	elif d == "D":
		old = posy
		posy -= c
		if posx in homeX:
			left = homeX[posx].bisect_left(posy)
			right = homeX[posx].bisect_left(old)
			ans -= right - left
			for i in range(left, right):
				y = homeX[posx].pop(left)
				homeY[y].remove(posx)
				if len(homeY[y]) == 0:
					del homeY[y]
				if len(homeX[posx]) == 0:
					del homeX[posx]
	elif d == "L":
		old = posx
		posx -= c
		if posy in homeY:
			left = homeY[posy].bisect_left(posx)
			right = homeY[posy].bisect_left(old)
			ans -= right - left
			for i in range(left, right):
				x = homeY[posy].pop(left)
				homeX[x].remove(posy)
				if len(homeX[x]) == 0:
					del homeX[x]
				if len(homeY[posy]) == 0:
					del homeY[posy]
	elif d == "R":
		old = posx
		posx += c
		if posy in homeY:
			left = homeY[posy].bisect_left(old)
			right = homeY[posy].bisect_left(posx)
			ans -= right - left
			for i in range(left, right):
				x = homeY[posy].pop(left)
				homeX[x].remove(posy)
				if len(homeX[x]) == 0:
					del homeX[x]
				if len(homeY[posy]) == 0:
					del homeY[posy]
	
	print(f"pos: {posx} {posy}")
					
print(posx, posy, N - ans)

