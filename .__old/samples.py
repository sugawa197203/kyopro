import heapq

def dijkstra(N:int, G:list[list[int,int]], s:int) -> list[float]:
	dist = [float("inf")] * N
	que = [(0, s)]
	dist[s] = 0
	while que:
		c, v = heapq.heappop(que)
		if dist[v] < c:
			continue
		for t, cost in G[v]:
			if dist[v] + cost < dist[t]:
				dist[t] = dist[v] + cost
				heapq.heappush(que, (dist[t], t))
	return dist

g = [
		[[1, 4], [2, 3]],
		[[2, 1], [3, 1], [4, 5]],
		[[5, 2]],
		[[4, 3]],
		[[6, 2]],
		[[4, 1], [6, 4]],
		[]
]

# 各ノードまでの最小コスト
print(dijkstra(7, g, 0))
