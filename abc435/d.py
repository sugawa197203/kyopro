from collections import defaultdict, deque

N, M = map(int, input().split())

G = defaultdict(list)

for _ in range(M):
    x, y = map(int, input().split())
    G[y].append(x)

Q = int(input())
isbrack = [False] * (N + 1)
for _ in range(Q):
    q, v = map(int, input().split())
    if q == 1:
        if isbrack[v]:
            continue
        isbrack[v] = True
        que = deque([v])
        while que:
            cv = que.popleft()
            for nv in G[cv]:
                if not isbrack[nv]:
                    isbrack[nv] = True
                    que.append(nv)
    else:
        print("Yes" if isbrack[v] else "No")

