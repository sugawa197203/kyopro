N, X = map(int, input().split())
A = list(map(int, input().split()))

flag = [False] * (N + 1)

ans = 0
_next = X

while True:
    if flag[_next]:
        break
    flag[_next] = True
    _next = A[_next - 1]


    ans += 1

print(ans)
