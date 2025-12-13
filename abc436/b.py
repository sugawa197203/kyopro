N = int(input())

G = [[None] * N for _ in range(N)]
r = 0
c = (N-1)//2
G[r][c] = 1
for k in range(2, N**2+1):
	if G[(r-1)%N][(c+1)%N] is None:
		r = (r-1)%N
		c = (c+1)%N
	else:
		r = (r+1)%N
	G[r][c] = k

for row in G:
	print(*row)
