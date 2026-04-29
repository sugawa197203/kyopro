from itertools import product

N, M = map(int, input().split())
lamps = []
for _ in range(M):
    k, *s = map(int, input().split())
    lamps.append(s)
P = list(map(int, input().split()))

ans = 0
for switch in product([0, 1], repeat=N):
    if all(sum(switch[i - 1] for i in lamp) % 2 == p for lamp, p in zip(lamps, P)):
        ans += 1

print(ans)
