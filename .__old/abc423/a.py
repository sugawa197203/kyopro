X, C = map(int, input().split())

ans = 0

for i in range(X // 1000):
    if ans * 1000 + C * ans <= X:
        ans += 1

if ans > 0:
    ans -= 1
print(ans * 1000)