import heapq

N, M = map(int, input().split())
A = list(map(int, input().split()))
U, V, B = [0]*M, [0]*M, [0]*M
for i in range(M):
	U[i], V[i], B[i] = map(int, input().split())

graph = [[] for _ in range(N)]
for i in range(M):
	graph[U[i]-1].append((V[i]-1, B[i]))
	graph[V[i]-1].append((U[i]-1, B[i]))

costFrom1 = [0]*(N-1)

def dijkstra(N:int, G:list[list[int,int]], s:int) -> list[float]:
	dist = [float("inf")] * N
	que = [(A[s], s)]
	dist[s] = A[s]
	while que:
		c, v = heapq.heappop(que)
		if dist[v] < c:
			continue
		for t, cost in G[v]:
			if dist[v] + cost + A[v] < dist[t]:
				dist[t] = dist[v] + cost + A[t]
				heapq.heappush(que, (dist[t], t))
	return dist
	
print(*dijkstra(N, graph, 0)[1:])