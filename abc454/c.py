from collections import defaultdict, deque

N, M = map(int, input().split())
AB = [tuple(map(int, input().split())) for _ in range(M)]

reachable = [False] * N

G = defaultdict(list)

for a, b in AB:
    G[a].append(b)

q = deque([1])

while q:
    v = q.popleft()
    if reachable[v - 1]:
        continue
    reachable[v - 1] = True
    for w in G[v]:
        q.append(w)

print(sum(reachable))
