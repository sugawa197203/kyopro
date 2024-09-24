import numpy as np

N, M = input().split(" ")
N = int(N)
M = int(M)

a = []

l = np.identity(N, int)

for i in range(M):
	a.append([int(b) for b in input().split(" ")])
for i in range(M):
	l[a[i][0]-1][a[i][1]-1] = 1
	for j in range(1, N - 1):
		l[a[i][j]-1][a[i][j+1]-1] = 1
		l[a[i][j]-1][a[i][j-1]-1] = 1
	l[a[i][-1]-1][a[i][-2]-1] = 1

c = 0

for i in range(N):
	for j in range(N):
		if l[i][j] == 0:
			c += 1
print(c//2)