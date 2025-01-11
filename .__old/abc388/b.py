N, D = map(int, input().split())
T, L = [], []
for _ in range(N):
	t, l = map(int, input().split())
	T.append(t)
	L.append(l)

for k in range(1, D+1):
	ans = 0
	for i in range(N):
		ans = max(ans, T[i] * (L[i] + k))
	
	print(ans)
