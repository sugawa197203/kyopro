import numpy as np

N = int(input())
pos = []
for i in range(N):
    x, y = map(int, input().split(" "))
    pos.append((x, y))

length = np.zeros((N, N))

for i in range(N):
	x = pos[i][0]
	y = pos[i][1]

	for j in range(N):
		_x = pos[j][0]
		_y = pos[j][1]
		dx = x - _x
		dy = y - _y
		length[i, j] = int(dx * dx + dy * dy)
		
print(np.sqrt(max(length.reshape((1, N * N))[0])))
