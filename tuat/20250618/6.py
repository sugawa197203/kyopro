N, M = map(int, input().split())
exist = set()
ans = 0
for _ in range(M):
    u, v = map(int, input().split())
    if u == v:
        ans += 1
        continue
    if (u, v) in exist:
        ans += 1
        continue
    exist.add((u, v))
    exist.add((v, u))

print(ans)