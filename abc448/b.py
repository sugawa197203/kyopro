N, M = map(int, input().split())
C = list(map(int, input().split()))
AB = [list(map(int, input().split())) for _ in range(N)]

ans = 0

for a, b in AB:
    use = min(C[a-1], b)
    ans += use
    C[a-1] -= use

print(ans)
