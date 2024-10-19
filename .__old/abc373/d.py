N, M = map(int, input().split())

edges = dict()
for i in range(N):
    edges[i] = []
for i in range(M):
    u, v, w = map(int, input().split())
    u -= 1
    v -= 1
    edges[u].append((v, w))
    edges[v].append((u, -w))

done = [False] * N
ans = [0] * N

for i in range(N):
    if done[i]:
        continue

    done[i] = True
    stack = [i]
    while stack:
        now = stack.pop()
        for next, w in edges[now]:
            if done[next]:
                continue
            done[next] = True
            ans[next] = w + ans[now]
            stack.append(next)

print(*ans)