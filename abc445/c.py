N = int(input())
A = list(map(int, input().split()))
watched = [0] * N
ans = [-1] * N

for n in range(N):
    if watched[n]:
        continue

    route = []
    pos = n
    while watched[pos] == 0:
        route.append(pos)
        watched[pos] = 1
        pos = A[pos] - 1
    
    if watched[pos] == 1:
        idx = route.index(pos)
        cycle = route[idx:]
        L = len(cycle)
        r = pow(10, 100, L)

        for i, v in enumerate(cycle):
            ans[v] = cycle[(i + r) % L]

    for v in reversed(route):
        if ans[v] == -1:
            ans[v] = ans[A[v] - 1]

    for v in route:
        watched[v] = 2

for a in ans:
    print(a + 1 if a + 1 != 0 else N, end=' ')
