from collections import defaultdict, deque

N, M = map(int, input().split())
G = defaultdict(list)
for _ in range(M):
    u, v = map(int, input().split())
    G[u].append(v)
    G[v].append(u)

distances = [float("inf")] * N
queue = deque([(1, 0)])
distances[0] = 0
while queue:
    node, dist = queue.popleft()
    for neighbor in G[node]:
        if distances[neighbor - 1] > dist + 1:
            distances[neighbor - 1] = dist + 1
            queue.append((neighbor, dist + 1))

for d in distances:
    print(d if d != float("inf") else -1)