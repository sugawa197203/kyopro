N = int(input())
A, B, C = map(int, input().split())

ans = 10000
for a in range(10000):
    for b in range(10000 - a):
        nokori = N - A * a - B * b
        if nokori < 0:
            break
        c, n = divmod(nokori, C)
        if n == 0:
            ans = min(ans, a + b + c)

print(ans)

