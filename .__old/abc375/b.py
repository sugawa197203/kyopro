N = int(input())
ans = 0.0
_a, _b = 0.0, 0.0
for i in range(N):
	a, b = map(int, input().split())
	dist = ((a - _a) ** 2 + (b - _b) ** 2) ** 0.5
	ans += dist
	_a, _b = a, b
dist = ((_a - 0) ** 2 + (_b - 0) ** 2) ** 0.5
ans += dist
print(ans)

