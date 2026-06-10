N, M = map(int, input().split())
AB = [tuple(map(int, input().split())) for _ in range(N)]

AB.sort(key=lambda x: x[0])

ans = 0

for a, b in AB:
    M -= b
    if M < 0:
        M += b
        ans += M * a
        break
    ans += b * a

print(ans)
