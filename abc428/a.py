S, A, B, X = map(int, input().split())
ans = 0
while A <= X:
    ans += S * A
    X -= A
    X -= B

if 0 < X:
    ans += S * X

print(ans)