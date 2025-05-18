N, K = map(int, input().split())
A = list(map(int, input().split()))

ans = 1
for a in A:
	ans *= a
	if len(str(ans)) > K:
		ans = 1
print(ans)