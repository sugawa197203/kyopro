from collections import defaultdict

N, M = map(int, input().split())
dist = [[float("inf")]*N for _ in range(N)]

for _ in range(M):
	u, v, w = map(int, input().split())
	dist[u-1][v-1] = min(dist[u-1][v-1], w)
	dist[v-1][u-1] = min(dist[v-1][u-1], w)

K, T = map(int, input().split())
D = list(map(int, input().split()))
for d in D:
	for dd in D:
		if d != dd:
			dist[d-1][dd-1] = min(dist[d-1][dd-1], T)
			dist[dd-1][d-1] = min(dist[dd-1][d-1], T)

Q = int(input())
for _ in range(Q):
	q = input().split()
	if q[0] == "1":
		x, y, t = map(int, q[1:])
		for i in range(N):
			for j in range(N):
				dist[i][j] = min(dist[i][j], dist[i][x-1] + t + dist[y-1][j])
				dist[i][j] = min(dist[i][j], dist[i][y-1] + t + dist[x-1][j])
	elif q[0] == "2":
		d = int(q[1])
		for x, y, in zip([d] * len(D), D):
			for i in range(N):
				for j in range(N):
					dist[i][j] = min(dist[i][j], dist[i][x-1] + T + dist[y-1][j])
					dist[i][j] = min(dist[i][j], dist[i][y-1] + T + dist[x-1][j])
	elif q[0] == "3":
		ans = 0
		for _dist in dist:
			for d in _dist:
				if d < float("inf"):
					ans += d
		print(ans)
			
