import heapq

def dijkstra(N:int, G:list[list[int,int]], s:int):
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

N = int(input())
A, B, X = [], [], []
for i in range(N-1):
    a, b, x = map(int, input().split())
    A.append(a)
    B.append(b)
    X.append(x)

edges = []

for i in range(N-1):
    edge = [[i+1, A[i]], [X[i]-1, B[i]]]
    edges.append(edge)
edges.append([])

print(dijkstra(N, edges, 0)[-1])
