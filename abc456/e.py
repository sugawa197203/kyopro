T = int(input())

from collections import defaultdict, deque

def solve(N: int, M: int, G: dict[int, list[int]], W: int, S: list[str]) -> bool:
    # print(N, M, G, W, S)
    # print("===========================")
    q = deque([(x, 0) for x in range(N) if S[x][0] == 'o'])
    

    watched = set()
    for x in range(N):
        watched.add((x, 0, S[x][0]))
    
    for t in range(W-1):
        # print("============")
        x, _t = q.popleft()

        # print(f"{x=}, {t=}, {watched=}, {q=}")

        for y in G[x]:
            if (y, t, 'o') in watched:
                print("1", y, t)
                return True
            watched.add((y, t, S[y][t]))
            if S[y][t] == 'o':
                q.append((y, t))
        
        if (x, t, 'o') in watched:
            print("2")
            return True

        watched.add((x, t, S[x][t]))
        if S[x][t] == 'o':
            q.append((x, t))

    return False

for _ in range(T):
    N, M = map(int, input().split())
    UV = [tuple(map(int, input().split())) for _ in range(M)]
    G = defaultdict(list)
    for u, v in UV:
        G[u - 1].append(v - 1)
        G[v - 1].append(u - 1)
    W = int(input())
    S = [input() for _ in range(N)]
    print('Yes' if solve(N, M, G, W, S) else 'No')
