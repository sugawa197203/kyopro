H, D = map(int, input().split())

ans = 0

while D > H:
    H *= 2
    ans += 1

print(ans)
