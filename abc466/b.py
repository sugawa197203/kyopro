N, M = map(int, input().split())
MM = [-1] * (M + 1)

for _ in range(N):
    c, s = map(int, input().split())
    MM[c] = max(MM[c], s)

print(*MM[1:])
